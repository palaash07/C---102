import cv2

def takeaScreenshot():
    #initialising cv2
    VideoCaptureObject = cv2.VideoCapture(0)
    result = True
    while(result):
        #read the frames while the camera is on 
        ret,frame = VideoCaptureObject.read()
        #cv2.imwrite() is used to save an image to any storage
        cv2.imwrite("newpicture.jpg",frame)
        result = False

    #release the camera
    VideoCaptureObject.release()
    #close the windows that might be open while in the process
    cv2.destroyAllWindows()    

takeaScreenshot()    
