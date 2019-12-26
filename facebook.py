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

username='enter your facebook id'
password = "enter your password facebook password"

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


