import numpy as np
import cv2
import argparse

from os import listdir,mkdir
from os.path import isfile, join

# Define the parser
parser = argparse.ArgumentParser(description='Short sample app')

# Declare an argument (`--path`), saying that the 
# corresponding value should be stored in the `ruta` 
# field, and using a default value if the argument 
# isn't given
parser.add_argument('--path', action="store", dest='ruta', default="None")

# Now, parse the command line arguments and store the 
# values in the `args` variable
args = parser.parse_args()

# Individual arguments can be accessed as attributes...
print (args.ruta)



mypath= args.ruta

onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
print(onlyfiles)


videoRuta=onlyfiles[0]
mkdir(videoRuta[:-4])

cap = cv2.VideoCapture(videoRuta)
frameNumber=0


while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    if ret== False:
        print("End of the video reached")
        break

    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Display the resulting frame
    cv2.imshow('frame',gray)
    cv2.imwrite(videoRuta[0:-4]+"/"+str(frameNumber)+".jpeg",gray)
    frameNumber+=1

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()

