import cv2
import  os
import numpy as np
import glob
cap = cv2.VideoCapture('osma.mp4')
i = 10
while True:
    _, img = cap.read()
    #img = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
    if img is None:
        break
    cv2.imwrite('dataset/selfie2anime/testA/frame'+str(i)+'.jpg',img)
    i = i + 1
cap.release()
os.system("python main.py --dataset selfie2anime --phase test")
i = 10
while True:
    newImage = cv2.imread('results/UGATIT_selfie2anime_lsgan_4resblock_6dis_1_1_10_10_1000_sn_smoothing/frame'+str(i)+'.jpg',flags=cv2.IMREAD_COLOR)
    if newImage is None:
        i = 10
        newImage = cv2.imread(
            'results/UGATIT_selfie2anime_lsgan_4resblock_6dis_1_1_10_10_1000_sn_smoothing/frame' + str(i) + '.jpg',
            flags=cv2.IMREAD_COLOR)
    cv2.imshow('img', newImage)
    i = i + 1
    k = cv2.waitKey(30) & 0xff
    if k==27:
        break

img_array = []
for filename in glob.glob('results/UGATIT_selfie2anime_lsgan_4resblock_6dis_1_1_10_10_1000_sn_smoothing/*.jpg'):
    img = cv2.imread(filename)
    height, width, layers = img.shape
    size = (width, height)
    img_array.append(img)

out = cv2.VideoWriter('prok.mp4', cv2.VideoWriter_fourcc(*'DIVX'), 15, size)

for i in range(len(img_array)):
    out.write(img_array[i])
out.release()