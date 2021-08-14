from bs4 import BeautifulSoup as bs
from selenium import webdriver
import selenium
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time
import random
import getpass 
import json
import os
from fake_useragent import UserAgent
import undetected_chromedriver.v2 as uc
import pyautogui

username = "der8ecker@icloud.com"
password = "9w97M#ZqT*fZf#eRZnZu!W5k"



URLCMC = "https://coinmarketcap.com/account/my-diamonds/"
PATH = "C:\Program Files (x86)\Chromedriver\chromedriver.exe"


ua = UserAgent()
userAgent = ua.random
print(userAgent)

def widthSmallerThen(width, value):
    if(width < value):
        return width
    else:
        return 1080

def set_viewport_size(driver):
    width = random.randint(1266, 1833)
    height = random.randint(856, widthSmallerThen(width, 1080))
    window_size = driver.execute_script("""
        return [window.outerWidth - window.innerWidth + arguments[0],
          window.outerHeight - window.innerHeight + arguments[1]];
        """, width, height)
    driver.set_window_size(*window_size)

# options = webdriver.ChromeOptions()
# options.add_argument("--start-maximized")
# options.add_argument(f'user-agent={userAgent}')
# driver = webdriver.Chrome(executable_path=PATH, chrome_options=options)
options = uc.ChromeOptions()
#options.add_argument("--start-maximized")
#options.add_argument(f'user-agent={userAgent}')
driver = uc.Chrome(options=options)
set_viewport_size(driver)
driver.delete_all_cookies()



def loginCMC():
    try:
        emailInput = WebDriverWait(driver, 5).until(
                        EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div/div[2]/div[3]/input[@type="email"]')))
        emailInput.clear()
        emailInput.send_keys(username)
        time.sleep(2)
        passwordInput = WebDriverWait(driver, 5).until(
                        EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div/div[2]/div[4]/div[2]/input[@type="password"]')))
        passwordInput.clear()
        passwordInput.send_keys(password)
        time.sleep(2)
        loginButton = WebDriverWait(driver, 5).until(
                        EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div/div[2]/div[6]/button')))
        loginButton.click()
    except:
        print("There was an error while trying to login")
    #finally:
        #set_viewport_size(driver)

def collectDiamonds():
    try:
        # #//*[@id="__next"]/div[1]/div[1]/div[1]/div[1]/div/div[2]/div[2]/nav/ul/li[1]/button
        # diamonds = WebDriverWait(driver, 5).until(
        #                     EC.presence_of_element_located((By.XPATH, '//*[@id="__next"]/div[1]/div[1]/div[1]/div[1]/div/div[2]/div[2]/nav/ul/li[1]/button')))
        # diamonds.click()
        # time.sleep(1) 
        collectButton = WebDriverWait(driver, 5).until(
                            EC.presence_of_element_located((By.XPATH, '//*[@id="__next"]/div/div[1]/div[2]/div/div/div[2]/div/div[2]/div[2]/div[1]/button')))
        collectButton.click()
        print("Button clicked")
    except:
        print("There was an error while trying to collect the diamonds")
           
try:
    driver.get(URLCMC)
    print(driver.execute_script('return navigator.webdriver'))
    print(driver.execute_script("return [window.innerWidth, window.innerHeight];"))
    time.sleep(2)
    loginCMC()
    time.sleep(3)
    pyautogui.hotkey('ctrl', 'shift', 'i')
    time.sleep(3)
    pyautogui.hotkey('ctrl', 'shift', 'i')
    driver.refresh()
    print("Logged in")
    #set_viewport_size(driver)
    driver.get(URLCMC)
    time.sleep(2)
    collectDiamonds()
finally:
    time.sleep(10)
    driver.quit()
    

time.sleep(10)





#COINGECKO

URLCG = "https://www.coingecko.com/account/candy?locale=de"

xpathtologinbuttoncg = '/html/body/div[2]/div[2]/div/div/div[6]/a[1]' # XPATH TO LOGIN BUTTON
xpathToButtoncg = '//*[@id="signInPassword"]' # XPATH TO COLLECT BUTTON
xpathtousernameloginfieldcg = '//*[@id="signInEmail"]' # XPATH TO LOGIN FIELD
xpathtopasswordloginfieldcg = '//*[@id="signInPassword"]' # XPATH TO PASSWORD FIELD





