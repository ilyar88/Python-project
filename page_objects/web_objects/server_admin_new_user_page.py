from selenium.webdriver.common.by import By

name = (By.ID,"name-input")
email = (By.ID,"email-input")
user_name = (By.ID,"username-input")
password = (By.ID,"password-input")
create_user = (By.CSS_SELECTOR,"button[type='submit']")

class ServerAdminNewUserPage():
    def __init__(self, driver):
        self.driver = driver

    def get_name(self):
        return self.driver.find_element(*name)

    def get_email(self):
        return self.driver.find_element(*email)

    def get_user_name(self):
        return self.driver.find_element(*user_name)

    def get_password(self):
        return self.driver.find_element(*password)

    def get_create_user(self):
        return self.driver.find_element(*create_user)