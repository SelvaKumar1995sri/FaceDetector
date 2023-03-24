import cv2

from random import randrange

#Load some pre-trained data on face frontals from opencv (haar cascade alogirthm)
trained_face_data = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

#choose an image to detect faces in
# img = cv2.imread('RDJ_1.png')

#To capture video from webcam
webcam = cv2.VideoCapture(0)
key = cv2.waitKey(1)

#iterates forever frames
while True:

    #read the current faces 
    successful_frame_read, frame = webcam.read()

    #must convert grayscale
    grayscaled_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    #detect faces
    face_coordinates = trained_face_data.detectMultiScale(grayscaled_img)

    #Draw a Rectangles around faces
    for (x,y,w,h) in face_coordinates:
        cv2.rectangle(frame, (x,y), ((x+w),(y+h)), (0,255,0), 2)


    cv2.imshow('clever progammer face detector',frame)
    key = cv2.waitKey(1)

    #stop when the Q key is pressed
    if key==81 or key==133:
        break

#release the webcamera object
webcam.release()


"""
#detect faces
face_coordinates = trained_face_data.detectMultiScale(grayscaled_img)

#Draw a Rectangles around faces
for (x,y,w,h) in face_coordinates:
    cv2.rectangle(img, (x,y), ((x+w),(y+h)), (randrange(256),randrange(256),randrange(256)), 2)

#print(face_coordinates)

#Display the image with faces
cv2.imshow('clever progammer face detector',img)
cv2.waitKey()


print("code completed")


"""