import os
class capture:
    def __init__(self,width, height, ip):
        self.width = width
        self.height = height
        self.ip = ip

    def launch():
        cmd = "gst-launch-1.0 rpicamsrc bitrate=1000000 ! 'video/x-h264,\
width="+self.width+",height="+self.height+"' ! h264parse ! queue ! rtph264pay config-interval=1 pt=96 ! gdppay ! \
udpsink host="+self.ip+" port=5000"
        os.system(cmd)
