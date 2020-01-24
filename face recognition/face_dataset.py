''''
Capture multiple Faces from multiple users to be stored on a DataBase (dataset directory)            

Based on original code by Anirban Kar: https://github.com/thecodacus/Face-Recognition    

Adapted from Marcelo Rovai - MJRoBot.org @ 21Feb18   
Developed by sinanSoysal - @ 24Jan20

'''

import cv2
import os

cam = cv2.VideoCapture(0)
cam.set(3, 640) # set video width
cam.set(4, 480) # set video height

# Creating a path called dataset
path="dataset"
try:
    os.mkdir(path)
except OSError:
    print ("Directory {} allready exists..".format(path))
else:
    print ("Successfully created the directory {} ".format(path))

face_detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

name_file=open("names.txt","a")

face_count=int(input("how many faces are you gonna add ==>  "))

for face_id in range(1,face_count+1):

    face_name = input('\n enter {}. user name ==>  '.format(face_id))
    name_file.write(face_name+"\n")

    print("\n [INFO] Initializing face capture. Look at the camera and wait ...")
    count = 0

    while(True):

        ret, img = cam.read()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_detector.detectMultiScale(gray, 1.3, 5)

        for (x,y,w,h) in faces:

            cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2)     
            count += 1

        # Save the captured image into the datasets folder
            cv2.imwrite("dataset/User." + str(face_id) + '.' + str(count) + ".jpg", gray[y:y+h,x:x+w])

            cv2.imshow('image', img)

        k = cv2.waitKey(100) & 0xff # Press 'ESC' for exiting video
        if k == 27:
            break
        elif count >= 30: # Take 30 face sample and stop video
            break

# Do a bit of cleanup
print("\n [INFO] Exiting Program and cleanup stuff")
name_file.close()
cam.release()
cv2.destroyAllWindows()


