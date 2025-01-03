from selenium.webdriver.common.by import By

user_name = (By.NAME,'user')
password = (By.ID,'current-password')
submit = (By.CSS_SELECTOR,"button[aria-label='Login button']")
skip = (By.CSS_SELECTOR,"button[aria-label='Skip change password button']")

class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def get_user_name(self):
        return self.driver.find_element(*user_name)

    def get_password(self):
        return self.driver.find_element(*password)

    def get_submit(self):
        return self.driver.find_element(*submit)

    def get_skip(self):
        return self.driver.find_elements(*skip)