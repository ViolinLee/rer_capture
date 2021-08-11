#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import cv2


cap = cv2.VideoCapture(0)

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc('M', 'J', 'P', 'G')
size = (1024, 768)
cap.set(6, fourcc)
cap.set(5, 30)  # May not implemented!
cap.set(3, size[0])
cap.set(4, size[1])

# Get FPS info
fps = int(cap.get(cv2.CAP_PROP_FPS))
print(fps)

out = cv2.VideoWriter('output.avi', fourcc, fps, size)
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    # write the flipped frame
    out.write(frame)
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) == ord('q'):
        break

# Release everything if job is finished
cap.release()
out.release()