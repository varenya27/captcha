from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

def isolateCaptcha(url):
    src=url[::-1]
    src=src[0:5]
    src=src[::-1]
    return src

#takes screenshot of aims page and saves it under the name of the captcha
def takess(link,n):
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get(link)
    # driver.set_window_size(1050, 787)
    time.sleep(3)

    # driver.close()
    for i in range(n):
        try:
            captcha = driver.find_element_by_id('appCaptchaLoginImg')
            src = isolateCaptcha(captcha.get_attribute('src'))
            s='testcases/del/'+src+'.png'
        except:
            driver.refresh()
            time.sleep(1)
            continue
        # print('saving at:',s)    

        driver.save_screenshot(s)
        driver.refresh()
        time.sleep(1)

link='https://aims.iith.ac.in/aims/'
# takess(link)
