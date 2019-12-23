import cv2
import numpy as np
cap = cv2.VideoCapture('vtest.avi')
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
const = 30
while True:
    status, img = cap.read()
    img = cv2.flip(img,0)
    faces = face_cascade.detectMultiScale(img, 1.3, 5)
    print("while öncesi"+str(faces))
    while len(faces)==0:
        print("Kerem buraya giriyor")
        img = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
        faces = face_cascade.detectMultiScale(img, 1.3, 5)
        print(faces)
    for (x, y, w, h) in faces:
        continue
        #x = x - const
        #y = y - const
        #yatay = x + w + (const * 2)
        #dikey = y + h + (const * 2)
        #if x < 0: x = 0
        #if y < 0: y = 0
        #if yatay > 256: yatay = 256
        #if dikey > 256: dikey = 256
        img = img[y:dikey, x:yatay]
    #img=cv2.rotate(img,cv2.ROTATE_90_CLOCKWISE)
    if img is None:
        break
    #cv2.imwrite('dataset/selfie2anime/testA/frame'+str(i)+'.jpg', cv2.flip(img,0))
    cv2.imshow('asdasd',img)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break
cap.release()

