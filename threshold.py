import cv2
import os

#thresholding
def threshold(img):
    # img = cv2.imread(imgpath)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ret, imgblack = cv2.threshold(img, 120, 255, cv2.THRESH_BINARY_INV)
    return imgblack
    # cv2.imwrite(imgpath,imgblack)
    # cv2.waitKey(0)

# folder=r'C:\Users\varen\OneDrive\coding\python\captcha\testcases\cropped'
# os.chdir(folder)
# i=0
# for image in os.listdir(folder):
#     threshold(image)


