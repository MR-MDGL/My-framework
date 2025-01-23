import time
from selenium import webdriver

from selenium.webdriver.common.by import By
driver = webdriver.Chrome()

driver.get("https://opensource-demo.orangehrmlive.com/")
time.sleep(10),'before login'
print(driver.title)                 # print title
print(driver.current_url)           # url of orangehrm after login
# print(driver.page_source)         to print print elements in dom
username_field = driver.find_element(By.XPATH, "//input[@placeholder='Username']")
username_field.send_keys("Admin")

password_field = driver.find_element(By.XPATH,"//input[@type='password']")
password_field.send_keys("admin123")

login_field = driver.find_element(By.XPATH,"//button[@type='submit']")
login_field.click()
time.sleep(2)
print(driver.title,'after login')     #after login title

time.sleep(5)

driver.close()
driver.quit()