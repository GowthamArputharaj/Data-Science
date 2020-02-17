#"C:\Users\Gowtham\AppData\Local\Programs\Python\Python38\Lib\site-packages\cv2\data\haarcascade_frontalface_default.xml"

import cv2
import numpy as np
import time

eye_detection=cv2.CascadeClassifier('C:\\Users\\Gowtham\\AppData\\Local\\Programs\\Python\\Python38\\Lib\\site-packages\\cv2\\data\\haarcascade_eye.xml')

face_detection=cv2.CascadeClassifier('C:\\Users\\Gowtham\\AppData\\Local\\Programs\\Python\\Python38\\Lib\\site-packages\\cv2\\data\\haarcascade_frontalface_default.xml')


#im = cv2.VideoCapture(0)
while True:
    im = cv2.VideoCapture(0)

    ret, frame = im.read()
    print(ret)

    cv2.imwrite("C:\\Users\\Gowtham\\Desktop\\abb.jpg",frame)
    #cv2.imshow("C:\\Users\\Gowtham\\Desktop\\abb.jpg",frame)
    #cv2.waitKey(0)
    print("before gray")
    img= cv2.imread("C:\\Users\\Gowtham\\Desktop\\abb.jpg")
    #img = cv2.imread("C:\\Users\\Gowtham\\Desktop\\ab.jpg")
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    print("after gray, before faces")

    eyes = eye_detection.detectMultiScale(gray, 1.3, 5)
    print("after faces, before for")
    for (x,y,w,h) in eyes:
        print("inside for, before rect")
        img=cv2.rectangle(img,(x,y),(x+w, y+h),(255,0,0),3)
        print("inside for, after rect")

    faces = face_detection.detectMultiScale(gray, 1.3, 5)
    print("after faces, before for")
    for (x,y,w,h) in faces:
        print("inside for, before rect")
        img=cv2.rectangle(img,(x,y),(x+w, y+h),(255,0,0),3)
        print("inside for, after rect")

    cv2.imwrite('C:\\Users\\Gowtham\\Desktop\\Face_AB.jpg',img)
    print("outside for, before imshow")
    cv2.imshow('D.E.T.E.C.T.E.D',img)
    cv2.imshow('C.A.P.T.U.R.E.D',frame)
    print("after imshow, before delay")
    #time.sleep(10)
    print("after delay")
    cv2.waitKey(0)
    im.release()
cv2.destroyAllWindows()

