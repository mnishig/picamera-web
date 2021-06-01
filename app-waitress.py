# app.py を flask-video-streaming のキャプチャ処理に差し替えてみる
# https://github.com/miguelgrinberg/flask-video-streaming/blob/master/camera.py

from util import gen_tempname

import io
import json
from threading import Condition
from time import sleep

from bottle import (
    Bottle, 
    response,
    run,
    static_file
)
import picamera

# from flask-video-streaming
import threading
from threading import get_ident
import time

class CameraEvent(object):
    def __init__(self):
        self.events = {}

    def wait(self):
        ident = get_ident()
        if ident not in self.events:
            self.events[ident] = [threading.Event(), time.time()]
        return self.events[ident][0].wait()

    def set(self):
        now = time.time()
        remove = None
        for ident, event in self.events.items():
            if not event[0].isSet():
                event[0].set()
                event[1] = now
            else:
                if now - event[1] > 5:
                    remove = ident

        if remove:
            del self.events[remove]

    def clear(self):
        self.events[get_ident()][0].clear()

class Camera(object):
    thread = None
    frame = None
    last_access = 0
    event = CameraEvent()

    def __init__(self):
        if Camera.thread is None:
            Camera.last_access = time.time()
            Camera.thread = threading.Thread(target=self.worker)
            Camera.thread.start()

            while self.get_frame() is None:
                time.sleep(0)

    def get_frame(self):
        Camera.last_access = time.time()
        Camera.event.wait()
        Camera.event.clear()
        return Camera.frame

    @staticmethod
    def frames():
        with picamera.PiCamera() as camera:
            camera.framerate = 5
            camera.resolution = (800, 600)

            time.sleep(2)

            stream = io.BytesIO()
            for _ in camera.capture_continuous(stream, 'jpeg', use_video_port=True):
                stream.seek(0)
                yield stream.read()

                stream.seek(0)
                stream.truncate()

    @classmethod
    def worker(cls):
        print('starting camera thread...')
        frames_ite = cls.frames()
        for frame in frames_ite:
            Camera.frame = frame
            Camera.event.set()
            time.sleep(0)

            if time.time() - Camera.last_access > 10:
                frames_ite.close()
                print('stopping camera thread due to inactivity')
                break
        
        Camera.thread = None
# end of from flask-video-streaming

HOST = '0.0.0.0'
PORT = 8080
DEBUG = True
TEMPLATE = 'app-waitress.html'
THREADS = 3

app = Bottle()

@app.route('/')
def index():
    return static_file(TEMPLATE, root='./')

@app.route('/config')
def config():
    return 'not implemented yet.'

@app.route('/take')
def take():
    print('/take: start...')
    # camera.wait_recording(3)
    with open(gen_tempname()+'.jpeg', 'wb') as f:
        frame = Camera().get_frame()
        print('frame:', len(frame))
        f.write(frame)

    response.headers['Content-Type'] = 'application/json'
    response.headers['Cache-Control'] = 'no-cache'
    return json.dumps({"ret": "take picture"})

def gen(camera):
    while True:
        frame = camera.get_frame()
        yield (
            b'--frame\r\n' +
            b'Content-Type: image/jpeg\r\n' + b'\r\n' +
            # b'Content-Length: ' + len(frame) + b'\r\n\r\n' + 
            frame + b'\r\n'
        )

@app.route('/streaming')
def streaming():
    response.headers['Content-Type'] = 'multipart/x-mixed-replace; boundary=frame'
    response.headers['Cache-Control'] = 'no-cache, private'
    response.headers['Pragma'] = 'no-cache'
    response.headers['Age'] = 0
    # return gen(CAMERA)
    return gen(Camera())


import waitress
waitress.serve(app, host=HOST, port=PORT, threads=THREADS)

