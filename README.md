# ece

## client
gst-launch-1.0 udpsrc port=5000 ! gdpdepay ! rtph264depay ! avdec_h264 ! videoconvert ! autovideosink sync=false

## pi
gst-launch-1.0 rpicamsrc bitrate=1000000     ! 'video/x-h264,width=640,height=480'     ! h264parse     ! queue     ! rtph264pay config-interval=1 pt=96     ! gdppay     ! udpsink host=[insert ip here] port=5000
