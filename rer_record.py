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
                cap = cv2.VideoCapture(-1)
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
                cnt = 0
                while int(datetime.now().hour) * 60 + int(datetime.now().minute) in minute_segment and cap.isOpened():
                    ret, frame = cap.read()
                    if not ret:
                        print("Can't receive frame (stream end?). Exiting ...")
                        break
                    # print("Debug: Successfully retieve frame.")
                    # cv2.imshow('frame', frame)
                    sleep(0.01)
                    try:
                        out.write(frame)
                    except Exception:  # Acchieve maximum size - 2GB
                        cnt += 1
                        out.release()
                        out_dir_suffix = out_dir.split('.avi')[0] + '_' + str(cnt) + '.avi'
                        out = cv2.VideoWriter(out_dir_suffix, fourcc, fps, (int(width), int(height)))
                        out.write(frame)

                print("Stop Recording.")
                cap.release()
                out.release()
                # cv2.destoryAllWindows()
                break

        # print("Not recording phase of time.")
        sleep(1)


class RunForever(object):
    def __init__(self):
        self.retry_cnt = 0

    def run_forever(self, root_dir):
        try:
            cam_record(root_dir)
        except Exception as err:
            self.retry_cnt += 1
            if self.retry_cnt > 10:
                os.system("reboot")

            self.handle_exception(err)
            self.run_forever(root_dir)

    def handle_exception(self, error):
        print(error)
        sleep(10)


if __name__ == "__main__":
    root_dir = "/data"

    contorller = RunForever()
    contorller.run_forever(root_dir)