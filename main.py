from use_google_drive import uploadImage
from use_camera import takeImage, show_preview, timelapse
from use_remote_stream import start_stream
from time import sleep
import datetime
#import thread
import threading
import sys

print('Start main!')

#image_name = takeImage()
#uploadImage(image_name)

#print("File " + image_name + " uploaded")
start_stream(1000)

#show_preview(5)
     
#print('Start!')
#timelapse(2, 420)

# Start processing requests for streaming function
print("1")
try:
    start_stream(600)
    
except KeyboardInterrupt:
    print("Shutdown of server on user request") 

finally:
    #image_name = takeImage()
    print('Done!')
    
takeImage()

print("Finally done!")