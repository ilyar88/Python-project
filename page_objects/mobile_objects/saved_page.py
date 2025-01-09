from selenium.webdriver.common.by import By

amount = (By.ID,'tvAmount')
term = (By.ID,'tvTerm')
rate = (By.ID,'tvRate')
delete = (By.ID,'btnDel')
confirm_delete = (By.XPATH,"//*[@text='OK']")

class SavedPage:
    def __init__(self, driver):
        self.driver = driver

    def get_amount(self):
        return self.driver.find_element(*amount)

    def get_term(self):
        return self.driver.find_element(*term)

    def get_rate(self):
        return self.driver.find_element(*rate)

    def get_delete(self):
        return self.driver.find_element(*delete)

    def get_confirm_delete(self):
        return self.driver.find_element(*confirm_delete)