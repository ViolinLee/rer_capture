import cv2
import numpy as np


cap = cv2.VideoCapture("/data/2021-08-13-20-00_1.avi")

if cap.isOpened() == False:
    print("Error Opening video File")

while cap.isOpened():
    ret, frame = cap.read()
    if ret == True:
        cv2.imshow("Frame", frame)
        if cv2.waitKey(25)&0xFF==ord("q"):
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()
