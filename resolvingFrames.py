import os
import cv2
def count_frames(path, override=False):
	# grab a pointer to the video file and initialize the total
	# number of frames read
	video = cv2.VideoCapture(path)
	total = 0
	# if the override flag is passed in, revert to the manual
	# method of counting frames
	if override:
		total = count_frames_manual(video)
	# otherwise, let's try the fast way first
	else:
		# lets try to determine the number of frames in a video
		# via video properties; this method can be very buggy
		# and might throw an error based on your OpenCV version
		# or may fail entirely based on your which video codecs
		# you have installed
		try:
			# check if we are using OpenCV 3
			if cv2.__version__=="4.4.0":
				total = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
			# otherwise, we are using OpenCV 2.4
			else:
				total = int(video.get(cv2.cv.CV_CAP_PROP_FRAME_COUNT))
		# uh-oh, we got an error -- revert to counting manually
		except:
			total = count_frames_manual(video)
	# release the video file pointer
	video.release()
	# return the total number of frames in the video
	return total

def count_frames_manual(video):
	# initialize the total number of frames read
	total = 0
	# loop over the frames of the video
	while True:
		# grab the current frame
		(grabbed, frame) = video.read()
	 
		# check to see if we have reached the end of the
		# video
		if not grabbed:
			break
		# increment the total number of frames read
		total += 1
	# return the total number of frames in the video file
	return total

def ProcessVideo(videPath):

    countedFrames=count_frames(videPath)
    print("This video has",countedFrames," frames")
    frameCounter=0
	
    cap= cv2.VideoCapture(videPath)
    while True:        
        # Capture frame-by-frame
        ret, frame = cap.read()
        if ret==False:
            break
        # Display the resulting frame
        cv2.imshow('frame',frame)
        cv2.imwrite(videPath[0:-4]+str(frameCounter)+".jpg",frame)
        frameCounter+=1


        #allowing the programmer to quit the process by pressing q
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # When everything done, release the capture
    cap.release()
    cv2.destroyAllWindows()

def main():
    dataSetPath="../dataSetEstadium"
    peoplesDataSet=os.listdir(dataSetPath)

        
    for personalDataSet in peoplesDataSet:
        print("Belonging to-->",personalDataSet)
        foldersContainingVideo= os.listdir(dataSetPath+"/"+personalDataSet)
        for videoFolder in foldersContainingVideo:
            print("Working on folder of the video-->",videoFolder)
            video=os.listdir(dataSetPath+"/"+personalDataSet+"/"+videoFolder)[0]
            print("Opening -->",video)
            videoPath=dataSetPath+"/"+personalDataSet+"/"+videoFolder+"/"+video
            ProcessVideo(videoPath)

            
        
    
main()