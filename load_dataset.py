import os
import cv2 as cv
from random import randint
from crop import crop #takes image path as input and crops it
from threshold import threshold #takes image path and thresholds it
from contour import isolate #splits the captcha based on boundaries and stores in bin
from screenshot import takess #takes ss and stores in testcases/more_raw/
name=0
link='https://aims.iith.ac.in/aims/'
n=5000
# takess(link,n)
def_path= os.getcwd()
folder = ''.join([os.getcwd(),r'\testcases\raw'])
os.chdir(folder)
for image in os.listdir(folder):
    # if name<=868:
    #     continue
    imgpath=os.path.abspath(image)
  
    # print(image)
    img=cv.imread(imgpath)
    # print(type(img))
    cropped=crop(img)
    # cv.imshow('img', cropped)
    # cv.waitKey(0)
    thresholded=threshold(cropped)
    # cv.imshow('img', thresholded)
    # cv.waitKey(0)
    list_of_letters= isolate(thresholded)
    captcha=imgpath[-9:-4]
    if isinstance(list_of_letters,int):
        print('Bad captcha:', captcha, list_of_letters)
        continue
    i=0
    for letter in list_of_letters:
        
        letter_folder=''.join(['Upper-',captcha[i].lower()]) if (captcha[i]).isupper() else ''.join(['Lower-',captcha[i].lower()])
    
        save_folder=''.join([def_path,r'\testcases\bin','\symbol-',letter_folder])
        if not os.path.exists(save_folder):
            os.mkdir(save_folder)   
        save_path= ''.join([save_folder,r'\id-',captcha,str(name),'.png'])
        # cv.imshow('img', letter)
        # cv.waitKey(0)
        try:
            cv.imwrite(save_path, letter)
        except:
            print(name, captcha)
        name+=1
        i+=1
        if i>4:
            i=0