from picamera import PiCamera
from time import sleep
from pathlib import Path

def capture():
    imgName = "image.jpg"

    camera = PiCamera()

    camera.start_preview()
    sleep(5)
    camera.capture(Path.cwd().joinpath(imgName))
    camera.stop_preview()

    return imgName