import cv2
from deepface import DeepFace
import os
from datetime import datetime

# Create screenshots folder
if not os.path.exists("screenshots"):
    os.makedirs("screenshots")

# Open webcam
cap = cv2.VideoCapture(0)

print("Press 'S' to save screenshot")
print("Press 'Q' to quit")

while True:

    ret, frame = cap.read()

    if not ret:
        break

    try:
        # Detect emotion
        result = DeepFace.analyze(
            frame,
            actions=['emotion'],
            enforce_detection=False
        )

        # Handle list/dict outputs
        if isinstance(result, list):
            result = result[0]

        emotion = result['dominant_emotion']
        emotions = result['emotion']

        confidence = emotions[emotion]

        # Draw text
        text = f"{emotion.upper()} ({confidence:.1f}%)"

        cv2.putText(
            frame,
            text,
            (20, 40),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0,255,0),
            2
        )
        y = 80
        for emo, score in emotions.items():
            cv2.putText(
                frame,
                f"{emo}: {score:.1f}%",
                (20, y),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.6,
                (255,255,255),
                2
            )
            y += 25

    except Exception:
        pass

    cv2.imshow("Real-Time Emotion Detection", frame)

    key = cv2.waitKey(1) & 0xFF

    # Save screenshot
    if key == ord('s'):
        filename = datetime.now().strftime("screenshots/%Y%m%d_%H%M%S.jpg")
        cv2.imwrite(filename, frame)
        print("Saved:", filename)

    # Quit
    elif key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()