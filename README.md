🎨 Air Drawing using OpenCV
📌 Project Overview

This project allows users to draw in the air using a colored object (like a blue pen). It tracks the object using computer vision and draws its movement on a virtual canvas in real time.

✨ Features
Real-time hand/object tracking using webcam
Draw in the air without touching the screen
Uses color detection (blue object)
Smooth drawing on virtual canvas
Clear canvas option
🛠️ Technologies Used
Python
OpenCV (cv2)
NumPy
📂 Project Structure
airdrawing.py   # Main script for air drawing
README.md       # Project documentation
▶️ How It Works
Captures video from webcam
Flips the frame for mirror effect
Converts frame to HSV color space
Detects blue color object
Finds contours of detected object
Tracks center point of object
Draws circles continuously on a canvas
Merges canvas with live video feed
🚀 Installation & Setup
1. Install dependencies
pip install opencv-python numpy
2. Run the project
python airdrawing.py
🖥️ Output
A window named "Air Drawing" will open
Move a blue object (pen/cap) in front of camera
Drawing will appear on screen following movement
⌨️ Controls
Press C → Clear the canvas
Press ESC → Exit the program
⚠️ Limitations
Works best with good lighting
Only detects blue color (can be modified)
Noise may occur if background has similar color
🔮 Future Improvements
Support multiple colors
Add brush thickness control
Save drawing as image
Use hand tracking (MediaPipe) instead of color detection
👨‍💻 Author

Ankit Singh
