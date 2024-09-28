from flask import Flask, render_template, Response
from picamera import PiCamera
import time
import io

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

def gen(camera):
    while True:
        time.sleep(0.1)
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/video_feed')
def video_feed():
    return Response(gen(Camera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

class Camera(object):
    def __init__(self):
        self.camera = PiCamera()
        self.camera.resolution = (640, 480)
        self.camera.framerate = 24

    def __del__(self):
        self.camera.close()

    def get_frame(self):
        stream = io.BytesIO()
        self.camera.capture(stream, 'jpeg', use_video_port=True)
        stream.seek(0)
        return stream.read()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True, threaded=True)
