from selenium.webdriver.common.by import By

class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    # Element locators
    username_field_NAME = "username"
    password_field_NAME = "password"
    login_button_XPATH = "//button[@type='submit']"
    invalid_login_message_XPATH = "//p[contains(@class,'oxd-alert-content-text')]"

    # Actions
    def enter_username(self, username):
        self.driver.find_element(By.NAME, self.username_field_NAME).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(By.NAME, self.password_field_NAME).send_keys(password)

    def click_login(self):
        self.driver.find_element(By.XPATH, self.login_button_XPATH).click()

    def get_invalid_login_message(self):
        return self.driver.find_element(By.XPATH, self.invalid_login_message_XPATH).text
