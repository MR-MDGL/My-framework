# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# driver = webdriver.Chrome()
# try:
#     driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
#     time.sleep(1)
#     textbox1 = driver.find_element(By.XPATH, "//input[@placeholder='Username']")
#     textbox1.send_keys("Admin")
#     time.sleep(1)
#     textbox2 = driver.find_element(By.XPATH, "//input[@placeholder='Password']")
#     textbox2.send_keys("admin123")
#     time.sleep(1)

#     click = driver.find_element(By.XPATH, "//button[@type='submit']")
#     click.click()
#     time.sleep(4)

#     expected = "Dashboard"
#     actual = driver.find_element(By.XPATH, "//h6[@class='oxd-text oxd-text--h6 oxd-topbar-header-breadcrumb-module']").text

#     if expected == actual:
#         print("Test case pass")
#     else:
#         print("Test case fail")

# except Exception as e:
#     print(f"An error occurred: {e}")

# finally:
#     driver.quit()
