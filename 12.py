from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("http://localhost:8081")

#check title
print("Title:", driver.title)

time.sleep(1)

#check fields
driver.find_element(By.ID,"name").send_keys("Zealo")
driver.find_element(By.ID,"email").send_keys("zealo@123")
driver.find_element(By.ID,"phno").send_keys("1234567890")

time.sleep(1)

#check button
driver.find_element(By.ID,"clickme").click()

alert = driver.switch_to.alert
print("Alert message:",alert.text)
alert.accept()
time.sleep(1)

print("Test passed succesfully")
driver.quit()