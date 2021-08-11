#!/usr/bin/env python3
# -*- coding:utf-8 -*-


import cv2
import os
from time import sleep
from datetime import datetime
from setting import minute_segments


def cam_record(root_dir):
    print("Record Service.")
    while True:
        time_now = datetime.now()
        minute = int(time_now.hour) * 60 + int(time_now.minute)

        for minute_segment in minute_segments:
            if minute in minute_segment:
                cap = cv2.VideoCapture(0)
                fourcc = cv2.VideoWriter_fourcc('M', 'J', 'P', 'G')
                size = (1024, 768)
                cap.set(6, fourcc)
                cap.set(5, 30)  # May not implemented!
                cap.set(3, size[0])
                cap.set(4, size[1])

                fps = int(cap.get(cv2.CAP_PROP_FPS))
                width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
                height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
                out_dir = os.path.join(root_dir, time_now.strftime("%Y-%m-%d-%H-%M") + '.avi')

                out = cv2.VideoWriter(out_dir, fourcc, fps, (int(width), int(height)))

                print("Start Recording.")
                while int(datetime.now().hour) * 60 + int(datetime.now().minute) in minute_segment and cap.isOpened():
                    ret, frame = cap.read()
                    if not ret:
                        print("Can't receive frame (stream end?). Exiting ...")
                        break
                    # print("Debug: Successfully retieve frame.")
                    # cv2.imshow('frame', frame)
                    sleep(0.01)
                    out.write(frame)

                print("Stop Recording.")
                cap.release()
                out.release()
                # cv2.destoryAllWindows()
                break

        # print("Not recording phase of time.")
        sleep(1)


def run_forever(root_dir):
    try:
        cam_record(root_dir)
    except Exception as err:
        handle_exception(err)
        run_forever(root_dir)


def handle_exception(error):
    print(error)
    sleep(5)


if __name__ == "__main__":
    root_dir = "/data"
    run_forever(root_dir)