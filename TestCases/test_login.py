import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest

@pytest.mark.smoke
def test_login():
    # Setting up Chrome options for headless mode
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")  # Run in headless mode
    options.add_argument("--disable-gpu")  # Disable GPU for better compatibility
    options.add_argument("--no-sandbox")  # Required for running in certain environments like Jenkins
    options.add_argument("--disable-dev-shm-usage")  # Overcomes limited resource issues

    driver = webdriver.Chrome(options=options)  # Initialize the WebDriver with the specified options

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
