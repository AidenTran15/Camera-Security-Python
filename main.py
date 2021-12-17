import cv2
import time
import datetime

cap = cv2.VideoCapture(0)

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
body_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_fullbody.xml")

dectection = True
dectection_stopped_time = None
timer_started = False
SECOND_TO_RECORD_AFTER_DETECTION = 5

# record the video
frame_size = (int(cap.get(3)), int (cap.get(4)))
fourcc = cv2.VideoWriter_fourcc(*"mp4v")
out = cv2.VideoWriter("video.mp4", fourcc, 20, frame_size)

while True:
    _, frame = cap.read()
    
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    bodies = face_cascade.detectMultiScale(gray, 1.3, 5)
    
    if len(faces) + len(bodies) > 0:
        if detection:
            timer_started = Fasler
        else:
            dectection = True
            current_time = datetime.datetime.now().strftime("%d-%m-%Y-%H-%M-%S")
            out = cv2.VideoWriter(f"{current_time}.mp4", fourcc, 20, frame_size)
        
    out.write(frame)
    
    #recognize the face with square
    for (x, y, width, height) in faces:
        cv2.rectangle(frame, (x,y), (x + width, y + height), (255, 0, 0), 3)
        
    cv2.imshow("Camera", frame)
    if cv2.waitKey(1) == ord('q'):
        break
    
out.release()    
cap.release()
cv2.destroyAllWindows()