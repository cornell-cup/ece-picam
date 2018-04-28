import picamera
import picamera.array
import socket
import time
class capture:
    def __init__(self,res,connec,time):
        self.res = res
        self.connec = connec
        self.time = time

    def rgbCapture(self):
        with picamera.PiCamera() as camera:
            with picamera.array.PiRGBArray(camera) as output:
                output.truncate(0)
                camera.resolution = self.res
                camera.capture(output, 'rgb')
                return output.array


    def vidCapture(self):
        client_socket = socket.socket()
        client_socket.connect((self.connec, 8000))
    
        connection = client_socket.makefile('wb')
        try:
            camera = picamera.PiCamera()
            camera.resolution = self.res
            camera.framerate = 30
            #time.sleep(2)
            camera.start_recording(connection, format='h264')
            camera.wait_recording(self.time)
            print time.time()
            camera.stop_recording()
        finally:
            connection.close()
            client_socket.close()

#print rgbCapture((1280,720))
#vidCapture('192.168.4.98',20)
obj1 = capture((640,480),'192.168.4.98',20)
#print obj1.rgbCapture()
obj1.vidCapture()
