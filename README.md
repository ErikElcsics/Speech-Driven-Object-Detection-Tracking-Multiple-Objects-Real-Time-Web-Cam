# Speech-Driven Object Tracker - Ask the AI what objects to find using your web camera

# Virtual Object Tracker - Object Detection and Voice Command Control - Ask the AI what objects to find using your web camera

Real-Time Object Detection with Voice Command Control—speech recognition for real-time object detection and tracking, including the ability to track multiple objects simultaneously. It highlights the real-time nature of the detection and the power of voice control.

This Python application uses **YOLOv8** for real-time object detection and allows users to track specific objects through voice commands. The application captures video from the webcam, performs object detection, and highlights detected objects on the video stream. The user can control which objects to track using voice commands, including compound commands (e.g., "Track bottle and chair").

## Summary

This project combines **YOLOv8**, **speech recognition**, and **OpenCV** to create a real-time object detection and tracking system. The user can issue voice commands to specify which objects (e.g., person, dog, car) they want the program to track. The application listens for these commands continuously, and once a valid object is recognized, it will track and highlight it in the video feed.

## Features

- **Real-Time Object Detection**: Detects and tracks objects from a live video feed using the **YOLOv8** model.
- **Voice Command Control**: Allows users to track specific objects by simply speaking commands.
- **Compound Commands**: Supports compound commands like "Track bottle and chair", where multiple objects can be tracked at once.
- **Detection Visualization**: Draws bounding boxes around detected objects and displays the object name.
- **Dynamic Object Selection**: Dynamically updates the list of tracked objects based on voice commands.
- **Timestamped Output**: Saves the processed video with detected objects as an AVI file, named with a timestamp.


### Objects you can ask to find in your Web Cam

- **Person**, **Bicycle**, **Car**, **Motorcycle**, **Airplane**, **Bus**, **Train**, **Truck**, **Boat**, **Traffic light**, **Fire hydrant**, **Stop sign**, **Parking meter**, **Bench**, **Bird**, **Cat**, **Dog**, **Horse**, **Sheep**, **Cow**, **Elephant**, **Bear**, **Zebra**, **Giraffe**, **Backpack**, **Umbrella**, **Handbag**, **Tie**, **Suitcase**, **Frisbee**, **Skis**, **Snowboard**, **Sports ball**, **Kite**, **Baseball bat**, **Baseball glove**, **Skateboard**, **Surfboard**, **Tennis racket**, **Bottle**, **Wine glass**, **Cup**, **Fork**, **Knife**, **Spoon**, **Bowl**, **Banana**, **Apple**, **Sandwich**, **Orange**, **Broccoli**, **Carrot**, **Hot dog**, **Pizza**, **Donut**, **Cake**, **Chair**, **Couch**, **Potted plant**, **Bed**, **Dining table**, **Toilet**, **TV**, **Laptop**, **Mouse**, **Remote**, **Keyboard**, **Cell phone**, **Microwave**, **Oven**, **Toaster**, **Sink**, **Refrigerator**, **Book**, **Clock**, **Vase**, **Scissors**, **Teddy bear**, **Hair dryer**, **Toothbrush**.

  
## Installation Instructions

Clone this repository:

git clone https://github.com/ErikElcsics/Virtual-Painter-App--Real-time-Hand-Tracking-Drawing-MediaPipe-App.git


### Requirements

Make sure you have **Python 3.6+** installed. Then, install the following dependencies:

pip install opencv-python numpy torch speechrecognition ultralytics


You will also need to download the **YOLOv8 model** from the official repository. You can use the `YOLO` model pre-trained weights (`yolov8n.pt`). The code will automatically do this for you.

## Example of Running

python speech_objects_tracker.py

## How the Code Works

### Object Detection

1. **YOLOv8 Model**: The application uses the **YOLOv8** model to detect objects from a live webcam feed.
2. **YOLO Classes**: It works with a predefined list of object classes (e.g., person, car, dog) for detection.
3. **Real-time Detection**: As the video feed is captured, the objects detected by YOLO are highlighted with bounding boxes.

### Voice Command

1. **Speech Recognition**: The application listens for voice commands using the **SpeechRecognition** library.
2. **Extract Object Names**: When a user speaks a command, the recognized speech is parsed to check for object names (e.g., "track person", "track car").
3. **Dynamic Tracking**: If a recognized object is part of the detection list, the system will start tracking it and display its bounding box.
4. **Compound Commands**: The app can handle compound commands, such as "Track bottle and chair," allowing you to track multiple objects at once.

### Workflow

- The system listens continuously for voice commands.
- When an object is detected in the video feed that matches the user's command, a bounding box is drawn around it.
- The program saves the video feed with the highlighted objects to a file.

## How to Use the App

1. Run the script. It will automatically open the webcam feed and start the detection process.
2. Speak a command to the system, such as "Track person" or "Track car".
3. The application will listen for objects to track and update the displayed video feed with bounding boxes for the tracked objects.
4. For compound commands, you can say things like "Track bottle and chair".
5. Press `q` to quit the program.

## Libraries Used

- **OpenCV**: For video capture, display, and object bounding.
- **PyTorch**: For running the YOLOv8 model for object detection.
- **SpeechRecognition**: For capturing and processing voice commands.
- **YOLOv8**: For object detection.

## Summary: User Perspective

- The app uses a webcam to detect objects in real time.
- The user can give voice commands to track specific objects.
- The detected objects are highlighted with bounding boxes on the webcam feed.
- Users can also use compound voice commands to track multiple objects at once.

## Summary: Technical Perspective

- **YOLOv8** is used for object detection, which identifies objects in the camera feed.
- **Speech recognition** listens for commands to change the objects to track.
- The detected objects are highlighted with bounding boxes, and the processed video is saved.
- **Threading** is used to run the voice command listener and object detection concurrently.

### YOLOv8 Object Detection
The YOLOv8n model (like the rest of the YOLOv8 family) is trained on the **COCO dataset**, which includes 80 common object categories. The app detects and tracks objects such as people, animals, vehicles, and everyday items.

- **YOLOv8**: Used for real-time object detection.
- **SpeechRecognition**: Used for voice command recognition.
