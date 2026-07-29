import cv2
import os
VIDEO_PATH = "19347491-hd_1920_1080_24fps.mp4"
PROCESS_WIDTH = 1280
PROCESS_HEIGHT = 720
if not os.path.isfile(VIDEO_PATH):
    print(f"Error: '{VIDEO_PATH}' not found. Place it in the same folder.")
    exit()
back_sub = cv2.createBackgroundSubtractorMOG2(history=500, varThreshold=50)
cap = cv2.VideoCapture(VIDEO_PATH)
if not cap.isOpened():
    print("Cannot open video.")
    exit()
print("Press 'q' to quit. Window resized to 1280x720.")
while True:
    ret, frame = cap.read()
    if not ret:
        print("End of video.")
        break
    frame = cv2.resize(frame, (PROCESS_WIDTH, PROCESS_HEIGHT))
    fg_mask = back_sub.apply(frame)
    fg_mask = cv2.morphologyEx(fg_mask, cv2.MORPH_OPEN, None)
    contours, _ = cv2.findContours(fg_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    for cnt in contours:
        if cv2.contourArea(cnt) > 500:
            x, y, w, h = cv2.boundingRect(cnt)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
    cv2.imshow("Cars & Moving Objects - Auto Sized", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()