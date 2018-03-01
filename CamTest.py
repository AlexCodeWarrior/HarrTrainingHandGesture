import picamera
import time

with picamera.PiCamera() as cam:
    cam.resolution=(1024,768)
    #start the preview of the camera
    cam.start_preview()
    #waits 5 seconds
    time.sleep(5)
    #captures image and save
    cam.capture('/home/pi/book/output/still.jpg')
