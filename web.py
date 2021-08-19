# coding:utf-8
import os
import cv2
import base64
import numpy as np
from flask import Flask, render_template, request


app = Flask(__name__)


def return_img_stream(img_local_path):
    with open(img_local_path, 'rb') as img_f:
        img_stream = img_f.read()
        img_stream = base64.b64encode(img_stream).decode()
    return img_stream


def get_recent_data():
    root = r'/data'
    filenames = os.listdir(root)
    if len(filenames):
        video_name = sorted(filenames, reverse=True)[0]
        video_path = os.path.join(root, video_name)
        cap = cv2.VideoCapture(video_path)
        if cap.isOpened():
            ret, frame = cap.read()
            cap.release()
            if ret == True:
                font = cv2.FONT_HERSHEY_SIMPLEX
                text = video_name.replace(".avi", "")
                cv2.putText(frame, text, (10, 30), font, 0.75, (0, 0, 255), 2)
                cv2.imwrite('img/color.png', frame)
                return 1
            else:
                return 0
        else:
            return 0
    else:
        return 0


@app.route('/api/vis')
def hello_world():
    code = get_recent_data()
    if code == 1:
        color_stream = return_img_stream('img/color.png')
        return render_template('simple_viewer.html', color_stream=color_stream)
    else:
        init_stream = return_img_stream('img/init.png')
        return render_template('simple_viewer.html', color_stream=init_stream)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=False, use_reloader=False)
