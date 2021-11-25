
import cv2
import dropbox
import time 
import random

starttime = time.time()

def takeaScreenshot():
    number = random.randint(0,100)
    videoCaptureObject = cv2.VideoCapture(0)
    result=  True

    while(result):
        ret,frame = videoCaptureObject.read()
        imgname = "img"+str(number)+".png"
        cv2.imwrite(imgname,frame)
        starttime = time.time()
        result = False

    return imgname
    print("screenshot taken ")
    videoCaptureObject.release()
    cv2.destroyAllWindows()    

def uploadFile(imgname):
    accestoken = "6z18r68eAzwAAAAAAAAAAUYsJ31bGAWc1RLbclaI3OWbYhwpOJEewmzrEKSTeG4G"
    file = imgname
    filefrom = file
    fileto = '/testfolder/'+(imgname)
    dbx = dropbox.Dropbox(accestoken)

    with open(filefrom,'rb') as f:
        dbx.files_upload(f.read(),fileto,mode = dropbox.files.WriteMode.overwrite)
        print("files uploading")

def main():
    while(True):
        if((time.time()-starttime)>= 5):
            name = takeaScreenshot()
            uploadFile(name)

main()            


