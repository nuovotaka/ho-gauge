import picamera
import datetime
from time import sleep

with picamera.PiCamera() as camera:
    print("Start Application...")

    # カメラの解像度を設定
    camera.resolution = (640, 480)
    # 撮影する前にカメラモジュールが完全に起動するのを待つ
    sleep(1)
    # 画像をキャプチャして、指定されたファイル名で保存する
    now = datetime.datetime.now()
    filename = '/home/pi/Pictures/image_' + now.strftime('%Y%m%d_%H%M%S') + '.jpg'
    camera.capture(filename)

    print("End Application")

