import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest

@pytest.mark.smoke  # Optional marker for categorization
def test_login():
    driver = webdriver.Chrome()
    try:
        # Open the OrangeHRM login page
        driver.get("https://opensource-demo.orangehrmlive.com/")
        time.sleep(2)

        print("Before login:", driver.title)  # Print title before login
        print("Current URL:", driver.current_url)

        # Perform login
        username_field = driver.find_element(By.XPATH, "//input[@placeholder='Username']")
        username_field.send_keys("Admin")

        password_field = driver.find_element(By.XPATH, "//input[@type='password']")
        password_field.send_keys("admin123")

        login_button = driver.find_element(By.XPATH, "//button[@type='submit']")
        login_button.click()

        time.sleep(2)
        print("After login:", driver.title)  # Print title after login

    finally:
        driver.close()
        driver.quit()
