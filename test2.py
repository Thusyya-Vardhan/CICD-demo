from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("http://localhost:8081")

#check title
print("Title:", driver.title)

time.sleep(2)

#check fields
driver.find_element(By.ID,"name").send_keys("Zealo")
driver.find_element(By.ID,"email").send_keys("zealo@123")
driver.find_element(By.ID,"phno").send_keys("1234567890")

time.sleep(2)

#check button
driver.find_element(By.CSS_SELECTOR,"button[type='submit']").click()

time.sleep(2)

print("Test passed succesfully")

driver.quit()