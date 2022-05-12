import os
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
import urllib.request
from solve import solvecaptcha
def isolateCaptcha(url):
    src=url[::-1]
    src=src[0:5]
    src=src[::-1]
    return src

#main code to log in 
#add a download thing and then send it to the captcha solver
#retreive the captcha from there and proceed

driver = webdriver.Chrome(ChromeDriverManager().install())
link='https://aims.iith.ac.in/aims/'

#hiding my shiz for obv reasons
creds = {'roll':'', 'pass':''}
with open('creds.txt', 'r') as f:
    for line in f:
        line=line.split()
        creds['roll']=line[0]
        creds['pass']=line[1]

# #firstpage
driver.get(link)
time.sleep(3)

enterUid = driver.find_element_by_id('uid')
enterUid.send_keys(creds['roll'])

enterPwd = driver.find_element_by_id('pswrd')
enterPwd.send_keys(creds['pass'])

captcha = driver.find_element_by_id('appCaptchaLoginImg')
src = isolateCaptcha(captcha.get_attribute('src'))

enterCaptcha = driver.find_element_by_id('captcha')
enterCaptcha.send_keys(src)

btn = driver.find_element_by_id('login')
btn.click()

#secondpage
# captcha1 = driver.find_element_by_id('appCaptchaLoginImg')
# src1 = isolateCaptcha(captcha1.get_attribute('src'))
# image=r'D:\coding\python\captcha\testcases\plswork\cap.png'
time.sleep(5)
while(1):
    img = driver.find_element_by_xpath('//*[@id="appCaptchaLoginImg"]')
    src = img.get_attribute('src')
    urllib.request.urlretrieve(src, "captcha.png")

    # driver.save_screenshot(image)
    text=solvecaptcha('captcha.png')
    if text!=0:
        break
    driver.refresh()
    time.sleep(2)
    
enterCaptcha = driver.find_element_by_id('captcha')
enterCaptcha.send_keys(text)

btn = driver.find_element_by_id('submit')
btn.click()

# driver.find_element_by_xpath('//*[@id="red"]/li/ul/li[5]/div').click()
# driver.find_element_by_xpath('//*[@id="red"]/li/ul/li[5]/ul/li[4]/span').click()
