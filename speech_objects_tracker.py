import cv2
import numpy as np
import torch
import speech_recognition as sr
from ultralytics import YOLO
import threading
import datetime

# Load YOLOv8 model
device = 'cuda' if torch.cuda.is_available() else 'cpu'
model = YOLO('yolov8n.pt').to(device)

# List of YOLO object classes
YOLO_CLASSES = [
    "person", "bicycle", "car", "motorcycle", "airplane", "bus", "train", "truck", "boat",
    "traffic light", "fire hydrant", "stop sign", "parking meter", "bench", "bird", "cat", "dog", "horse",
    "sheep", "cow", "elephant", "bear", "zebra", "giraffe", "backpack", "umbrella", "handbag", "tie",
    "suitcase", "frisbee", "skis", "snowboard", "sports ball", "kite", "baseball bat", "baseball glove",
    "skateboard", "surfboard", "tennis racket", "bottle", "wine glass", "cup", "fork", "knife", "spoon",
    "bowl", "banana", "apple", "sandwich", "orange", "broccoli", "carrot", "hot dog", "pizza", "donut",
    "cake", "chair", "couch", "potted plant", "bed", "dining table", "toilet", "tv", "laptop", "mouse",
    "remote", "keyboard", "cell phone", "microwave", "oven", "toaster", "sink", "refrigerator", "book",
    "clock", "vase", "scissors", "teddy bear", "hair drier", "toothbrush"
]

# Globals
target_objects = []

def extract_objects_from_command(command):
    command = command.lower()
    return [cls for cls in YOLO_CLASSES if cls in command]

def listen_for_commands():
    global target_objects
    recognizer = sr.Recognizer()
    mic = sr.Microphone()

    with mic as source:
        recognizer.adjust_for_ambient_noise(source)

    while True:
        with mic as source:
            print("🎤 Listening for object commands...")
            audio = recognizer.listen(source)
        try:
            command = recognizer.recognize_google(audio)
            print(f"🔊 Heard: {command}")
            extracted = extract_objects_from_command(command)
            if extracted:
                target_objects = extracted
                print(f"🎯 Tracking: {', '.join(target_objects)}")
            else:
                print("⚠️ No known objects recognized in the command.")
        except sr.UnknownValueError:
            print("🤷 Could not understand audio.")
        except sr.RequestError as e:
            print(f"❌ Speech recognition error: {e}")

def run_detection():
    cap = cv2.VideoCapture(0)

    # Set up video writer
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    out = cv2.VideoWriter(f"detected_output_{timestamp}.avi", fourcc, 20.0, (640, 480))

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        results = model(frame, verbose=False)[0]
        for box in results.boxes:
            cls_id = int(box.cls[0])
            class_name = YOLO_CLASSES[cls_id]

            if class_name in target_objects:
                x1, y1, x2, y2 = map(int, box.xyxy[0])
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
                cv2.putText(frame, class_name, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

        out.write(frame)
        cv2.imshow("🔍 Object Detection", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    out.release()
    cv2.destroyAllWindows()

# Start continuous speech recognition in a separate thread
threading.Thread(target=listen_for_commands, daemon=True).start()

# Start object detection
run_detection()
