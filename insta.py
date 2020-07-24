
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import pandas as pd

df = pd.read_csv (r'file path of instagram username')

#print (df)

#####****Setting up chrome and Instagram for primary login****#####

webdriver =  webdriver.Chrome("C:\webdrivers\chromedriver.exe")
sleep(2)
webdriver.get('https://www.instagram.com/direct/inbox/')
sleep(3)

username = webdriver.find_element_by_name('username')
username.send_keys('sitaram_xyz')

password = webdriver.find_element_by_name('password')
password.send_keys('Warner@31')

#Login in by clicking Enter
password.send_keys(Keys.ENTER)
sleep(3)

webdriver.back()
sleep(3)

# 1 Notifications- Not Now button click
webdriver.find_element_by_xpath('//*[@class= "aOOlW   HoLwm "]').click()
sleep(2)

list1 = df.values.tolist()
#list1 = ["ja9942885", "lakshmi.rupaa"]
for i in list1:
    # 2 New message Icon click
    webdriver.find_element_by_xpath('//*[@class="wpO6b ZQScA"]').click()
    sleep(2)

    # 3 Enter username in Search box
    text_input = webdriver.find_element_by_xpath('//*[@name="queryBox"]')
    text_input.send_keys(i)
    sleep(2)
    # 4 Select the first user
    webdriver.find_element_by_xpath('//*[@class= "glyphsSpriteCircle__outline__24__grey_2 u-__7"]').click()
    sleep(2)
    # 5 Click Next
    webdriver.find_element_by_xpath('//*[@class= "sqdOP yWX7d    y3zKF   cB_4K  "]').click()
    sleep(2)
    # 6 Selecting the MESSAGE box and typing into it.
    message_box = webdriver.find_element_by_xpath('//*[@class= "focus-visible"]')
    message_box.send_keys('test')
    sleep(2)
    message_box.send_keys(Keys.ENTER)
    sleep(2)


#webdriver.find_element_by_xpath('//*[@class="wpO6b ZQScA"]').click()
#sleep(2)
#webdriver.find_element_by_xpath('//*[@name="queryBox"]').send_keys('vatsavvatsav')
#sleep(3)
#webdriver.find_element_by_xpath('//*[@class= "glyphsSpriteCircle__outline__24__grey_2 u-__7"]').click()
#sleep(2)
#webdriver.find_element_by_xpath('//*[@class= "sqdOP yWX7d    y3zKF   cB_4K  "]').click()
#sleep(2)


#webdriver.get('https://www.instagram.com/direct/new/')
#sleep(8)

#sleep(5)
                    ######**** IG Search Box ****######

#search = webdriver.find_element_by_xpath("//input[@placeholder='Search']")
#search.send_keys('SearchEntry')
#sleep(3)
#Selecting First Search Profile
#webdriver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/div[3]/div[2]/div/a').send_keys(Keys.ENTER)
#sleep(5)

# Message Button click (In case if primary profile follows the other profile)
#webdriver.find_element_by_xpath('//*[@class= "fAR91 sqdOP  L3NKy _4pI4F   _8A5w5    "]').click()
#sleep(3)

#Alternate Login Hit button
#submit = webdriver.find_element_by_tag_name('form')
#submit.submit()