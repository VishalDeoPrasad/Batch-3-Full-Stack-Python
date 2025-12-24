
import cv2

# Load Haar cascade for face detection
face_cascade = cv2.CascadeClassifier(
cv2.data.haarcascades + 
"haarcascade_frontalface_default.xml")

cap = cv2.VideoCapture(0)

first_face = None  # To store first detected face ROI

while True:
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(80, 80))

    if len(faces) >= 2:
        # Take first and second faces
        (x1, y1, w1, h1) = faces[0]
        (x2, y2, w2, h2) = faces[1]

        face1 = frame[y1:y1 + h1, x1:x1 + w1]
        face1_resized = cv2.resize(face1, (w2, h2))

        # Create a copy of frame
        frame_swap = frame.copy()

        # Replace second face with first face
        frame_swap[y2:y2 + h2, x2:x2 + w2] = face1_resized

        # Draw rectangles for visualization
        cv2.rectangle(frame_swap, (x1, y1), (x1 + w1, y1 + h1), (255, 0, 0), 2)
        cv2.rectangle(frame_swap, (x2, y2), (x2 + w2, y2 + h2), (0, 255, 0), 2)

        cv2.imshow("Face Swap (Basic)", frame_swap)

    else:
        cv2.imshow("Face Swap (Basic)", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
