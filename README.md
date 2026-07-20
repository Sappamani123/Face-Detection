

Face Detection using OpenCV | Python

  This project implements real-time face detection using the OpenCV library and Haarcascade classifiers. The webcam feed is captured and processed to detect human faces, which are highlighted     with bounding boxes.

🚀 Features

   -Real-time face detection

   -Uses Haarcascade XML model

   -Fast and lightweight

   -Beginner-friendly Python code

🛠 Technologies Used
 
   -Python 3

   -OpenCV (cv2)

   -Haarcascade Models (built-in with OpenCV)
   
🧠 How It Works

   Loads Haarcascade for face detection:
   
   cascade_classifier = cv2.CascadeClassifier(
      cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
   )

   -Captures webcam frames

   -Converts each frame to grayscale
   
   -Applies detectMultiScale() to detect faces

   -Draws rectangles around detected faces

   -Displays the real-time output

📸 Output

   -Automatically detects faces in live video

   -Blue rectangle drawn around detected face(s)
  


https://github.com/user-attachments/assets/885df354-72e3-481a-9923-b672e3b470e3




