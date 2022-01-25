import cv2
import os
from os import listdir
#cropping the landing page to give captcha
def crop(img):
    #default dimensions: 1341x854
    # img = cv2.imread(imgpath)

    # cv2.imshow('Image', image)
    #for atharv's pc
    # y=475
    # x=750
    # h=70
    # w=290

    #for my laptop
    y=100
    x=270
    h=60
    w=260
    
    cropped_img = img[y:y+h, x:x+w]
    return cropped_img
    # cv2.imshow('Image', cropped_img)
    # img=imgpath.replace('raw','cropped')
    # cv2.imwrite(imgpath,crop)
    # cv2.waitKey(0)

# folder=r'C:\Users\varen\OneDrive\coding\python\captcha\testcases\cropped'
# os.chdir(folder)
# i=0
# for image in os.listdir(folder):
#     i+=1
#     if i<=5:
#         continue
#     crop(imgpath=image) 
img=r'D:\coding\python\captcha\testcases\plswork\cap.png'
img=cv2.imread(img)
crop(img)
