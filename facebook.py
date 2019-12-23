from selenium import webdriver 
import pprint, requests
from time import sleep 
from getpass import getpass
from bs4 import BeautifulSoup
import time
  
username='username'
# password=input('Enter Password:')           #show password
password = "password"       #hide password

driver = webdriver.Chrome("./chromedriver") 
prefs = {"profile.default_content_setting_values.notifications" : 3} # to hide browser notifications
url= 'https://www.facebook.com/'
driver.get(url) 
print ("Opened facebook") 
sleep(1) 
  
username_box = driver.find_element_by_id('email') 
username_box.send_keys(username) 
print ("Email Id entered") 
sleep(1) 
  
password_box = driver.find_element_by_id('pass') 
password_box.send_keys(password) 
print ("Password entered") 
#   
login_box = driver.find_element_by_id('loginbutton') 
login_box.click() 


place="delhi"
market_url= url+ 'marketplace/'+ place 
driver.get(market_url)

item_url= url + '/marketplace' + '/item/2381441782185456/'
data=driver.get(item_url)
# print(data)

print("message print")
print("plz wait")
time.sleep(5)

# button=driver.find_element_by_css_selector('#js_8 > div:nth-child(2) > div._3-98 > div > div > div > div > div._3qny._4bl7 > div > div._1ol4 > div.center._2pi0._1lil > div > div._3-8y > button')
button=driver.find_element_by_xpath('//*[@id="js_8"]/div[2]/div[1]/div/div/div/div/div[2]/div/div[2]/div[1]/div/div[4]/button')
button.click()

print("message sent successfully!")
input('Press anything to quit') 
driver.quit()
