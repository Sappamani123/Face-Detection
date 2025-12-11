import cv2
cascade_classifier = cv2.CascadeClassifier(
    cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
)
cap = cv2.VideoCapture(0)  # webcam
while True:
    ret, frame = cap.read()
    if not ret:
        break
    # Convert to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # Detect faces
    detections = cascade_classifier.detectMultiScale(
        gray,
        scaleFactor=1.3,
        minNeighbors=5
    )
    # Draw rectangle around first detected face
    for (x, y, w, h) in detections:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
        break  # only first face
    # Show output
    cv2.imshow('frame', frame)
    # Quit on pressing 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
