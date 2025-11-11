from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver=webdriver.Chrome()

driver.get("http://bing.com")

print("Opened Page:",driver.title)

search=driver.find_element(By.NAME,'q')
search.send_keys("selenium tutorial")
search.send_keys(Keys.RETURN)

time.sleep(3)

print("Opened page:",driver.title)

if "selenium" in driver.title:
    print("Test passed")
else:
    print("Test failed")
