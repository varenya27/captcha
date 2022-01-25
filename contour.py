import cv2 
import numpy as np
import os
from random import randint

#takes path to folder with all cropped and thresholded images
#makes folders for each symbol separately
def isolate(img):
    # captcha=imgpath[-9:-4]
    # img=cv2.imread(imgpath)
    # img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    contours, hierarchy = cv2.findContours(img, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    # cnt=contours[7]
    # cv2.drawContours(img,[i], 0, (0,255,0), 3)
    l=[]
    for cnt in contours:
        x,y,w,h = cv2.boundingRect(cnt)
        # print(x,y,w,h)
        if (w>26 and w<60 and h>19 and h<60) or (w<=26 and h>20) or ():
        # if(1):
            cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,0),0)
            l.append((x,y,w,h))
 
    # cv2.imshow('windwo', img)
    # cv2.waitKey(0)
    l = sorted(l, key=lambda x: x[0])
    i=0
    letters=[]
    for x,y,w,h in l:
        letter_image = img[y - 2:y + h + 2, x - 2:x + w + 2]
        letters.append(letter_image)
        # cv2.imshow('pls work', img)
        # cv2.waitKey(0)
        i+=1
    # for im in letters:
        # cv2.imshow('vbdf', im)
        # cv2.waitKey(0)
    if(len(letters)!=5):
    # if(1):
        # cv2.imshow('windwo', img)
        # cv2.waitKey(0)
        # for im in letters:
        #     cv2.imshow('vbdf', im)
        #     cv2.waitKey(0)
        #     print('failed')
        # for x,y,w,h in l:
        #     print('w:',w,', h:',h)
        
        return len(letters)
    return letters    

# folder=r'C:\Users\varen\OneDrive\coding\python\captcha\testcases\thresholded'
# os.chdir(folder)
# i=0
# for image in os.listdir(folder):
#     # if i==1:
#     #     break
#     try:
#         isolate(imgpath=image)
#     except:
#         continue 
