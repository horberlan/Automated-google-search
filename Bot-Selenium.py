import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome() # Here you need the specific selenium PATH webdriver for each browser and you can find it here (https://www.selenium.dev/documentation/en/getting_started_with_webdriver/browsers/). In a linux environment, you will extract the .zip file and insert it in the folder //usr/local/bin and ready, it's already working.
PROXY = "169.57.157.148:80" # Proxy port and IP address, you will find the link (https://hidemy.name/en/proxy-list/?country=BR&type=hs&anon=4#list) they don't stay on the air for more than a day, so you have to change them whenever possible. I usually use port 80 or 8080.
webdriver.DesiredCapabilities.CHROME['proxy'] = {
    "httpProxy":PROXY,
    "proxyType":"MANUAL" # 
 }
driver.get("https://www.google.com")
time.sleep(1)
# These are the places accessed on the page and the CSS classes and HTML tags are collected, just type CTRL + U and search for what you want to link.

enter_searchbar = driver.find_element_by_class_name("gLFyf.gsfi")
enter_searchbar.send_keys(f"horberlan · Github")
enter_searchbar.send_keys(Keys.ENTER) # emulate the enter key.
time.sleep(1.5)
click_link1 = driver.find_element_by_class_name("LC20lb.DKV0Md")
click_link1.click()
time.sleep(1)
click_link12 = driver.find_element_by_link_text("Selenium-Python_bot_Google")
click_link12.click()   
# span.repo
time.sleep(300)

driver.close()
#This is very basic. You can redo as per your need. Thanks!