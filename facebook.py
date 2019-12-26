from selenium import webdriver 
import pprint, requests
from time import sleep 
from getpass import getpass
from bs4 import BeautifulSoup
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

option = Options()                          
# option.add_argument("--disable-infobars")
option.add_argument("start-maximized")
option.add_argument("--disable-extensions")      #"**--disable-notifications**"
option.add_argument("--disable-notifications")

username='8826616653'
password = open("password", "r").read()

driver = webdriver.Chrome("./chromedriver", chrome_options=option)
url= 'https://www.facebook.com/'
driver.get(url) 
print ("Opened facebook") 
sleep(4) 
driver.maximize_window()
sleep(2) 

username_box = driver.find_element_by_id('email') 
username_box.send_keys(username) 
print ("Email Id entered") 
sleep(1) 
  
password_box = driver.find_element_by_id('pass') 
password_box.send_keys(password) 
print ("Password entered") 

login_box = driver.find_element_by_id('loginbutton') 
login_box.click() 
print("login sucessfully!")


place="delhi"
market_url= url+ 'marketplace/'+ place 
driver.get(market_url)

item_url= url + '/marketplace' + '/item/813886775703571/'
data=driver.get(item_url)

print("message print")
print("plz wait")
time.sleep(5)

#sent a message 
# newMessage=driver.find_element_by_css_selector('#js_8 > div:nth-child(2) > div._3-98 > div > div > div > div > div._3qny._4bl7 > div > div._1ol4 > div.center._2pi0._1lil > div > div._3-8y > button')
messageAgain=driver.find_element_by_xpath('//*[@id="js_3"]/div[2]/div[1]/div/div/div/div/div[2]/div/div[2]/div[1]/div/button')

# time.sleep(2)
# if(button==button):
# newMessage.click()
# print("message sent successfully!")
# input('Press anything to quit') 
# # driver.close()
# driver.quit()

# else:
#again sent a message or chat
messageAgain.find_element_by_xpath('//*[@id="js_3"]/div[2]/div[1]/div/div/div/div/div[2]/div/div[2]/div[1]/div/button')
sleep(3)                        
messageAgain.send_keys("what is the price", Keys.ENTER)
input('Press anything to quit') 
# driver.close()
driver.quit()














# from selenium import webdriver 
# import pprint, requests
# from selenium.webdriver.support.ui import Select
# from selenium.webdriver.common.keys import Keys
# from time import sleep 
# from getpass import getpass
# from bs4 import BeautifulSoup
# import time
  
# username='8826616653'                        
# # password=input('Enter Password:')           #show password
# password = open("password", "r").read()       #hide password

# driver = webdriver.Chrome("./chromedriver") 
# prefs = {"profile.default_content_setting_values.notifications" : 3} # to hide browser notifications
# url= 'https://www.facebook.com/'
# driver.get(url) 
# print ("Opened facebook") 
# sleep(1) 
  
# username_box = driver.find_element_by_id('email') 
# username_box.send_keys(username) 
# print ("Email Id entered") 
# sleep(1) 
  
# password_box = driver.find_element_by_id('pass') 
# password_box.send_keys(password) 
# print ("Password entered") 
# #   
# login_box = driver.find_element_by_id('loginbutton') 
# login_box.click() 


# place="delhi"
# market_url= url+ 'marketplace/'+ place 
# # driver.get(market_url)

# item_url= url + '/marketplace' + '/item/2381441782185456/'
# data=driver.get(item_url)
# print("plz wait")
# sleep(5)
# driver.execute_script('return document.documentElement.outerHTML')
# # print(page)
# # driver.implicitly_wait(5)
# driver.find_element_by_tag_name("button").click()
# # driver.find_element_by_link_text("Message")
# driver.find_element_by_class_name("_2x3t _3dqo _645h")
# # driver.find_element_by_xpath('')
# # driver.find_element_by_xpath('//*[@id="js_s"]/div[2]/div[1]/div/div/div/div/div[2]/div/div[2]/div[2]/div/div/div/div/div/div[1]/div/span').click()
# print("message sent successfully!")
# input('Press anything to quit') 
# driver.quit()

