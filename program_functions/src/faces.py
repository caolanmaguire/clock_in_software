import numpy as np
import cv2
import pickle
from datetime import date
from datetime import datetime

face_cascade = cv2.CascadeClassifier('cascades/data/haarcascade_frontalface_alt2.xml')
eye_cascade = cv2.CascadeClassifier('cascades/data/haarcascade_eye.xml')
smile_cascade = cv2.CascadeClassifier('cascades/data/haarcascade_smile.xml')


recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read("./recognizers/face-trainner.yml")

labels = {"person_name": 1}
with open("pickles/face-labels.pickle", 'rb') as f:
    og_labels = pickle.load(f)
    labels = {v:k for k,v in og_labels.items()}

cap = cv2.VideoCapture(0)

clock_in_record = '\nClock in record: ' + str(datetime.today().strftime('%Y-%m-%d')) + '\n'
current_attention = {}

while(True):
    # Capture frame-by-frame from video.
    ret, frame = cap.read()
    gray  = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.5, minNeighbors=5)
    for (x, y, w, h) in faces:
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]

        id_, conf = recognizer.predict(roi_gray)
        if conf>=4 and conf <= 85:
            font = cv2.FONT_HERSHEY_SIMPLEX
            name = labels[id_]
            color = (255, 255, 255)
            stroke = 2
            cv2.putText(frame, name + ' ' + datetime.now().strftime("%H: %M : %S"), (x,y), font, 1, color, stroke, cv2.LINE_AA)
            right_now = str(datetime.now().strftime("%H: %M")) + ''
            if name in current_attention:
                 minutes_since_last = int(right_now.split(' ')[1]) - int(current_attention[name].split(' ')[1])
                 if minutes_since_last > 1:
                    current_attention[name] = right_now
                    clock_in_record = clock_in_record + '\n' + 'Employee then seen at :' + name + ', Time:' + right_now
            else:
                 #print('new face')
                 current_attention[name] = right_now
                 clock_in_record = clock_in_record + '\n' + 'Employee clocked in at :' + name + ', Time:' + right_now

        img_item = "7.png"
        cv2.imwrite(img_item, roi_color)

        color = (255, 0, 0)  
        stroke = 2
        end_cord_x = x + w
        end_cord_y = y + h
        # cv2.rectangle(frame, (x, y), (end_cord_x, end_cord_y), color, cv2.FILLED)
        
        shapes = np.zeros_like(frame, np.uint8)

        cv2.rectangle(shapes, (x, y), (end_cord_x, end_cord_y), (255, 255, 255), cv2.FILLED)



        # Display the resulting frame
        out = frame.copy()
    alpha = 0.5
    mask = shapes.astype(bool)
    out[mask] = cv2.addWeighted(frame, alpha, shapes, 1 - alpha, 0)[mask]

    cv2.imshow('frame2',out)
    # cv2.imshow('frame',frame)
    if cv2.waitKey(20) & 0xFF == ord('q'):
        print(clock_in_record)
        database = open("database.csv", "a")  # append mode
        database.write(clock_in_record)
        database.close()
        break

# When all check in frame done show capture
cap.release()
cv2.destroyAllWindows()