from selenium.webdriver.common.by import By

amount = (By.ID,'etAmount')
term = (By.ID,'etTerm')
rate = (By.ID,'etRate')
calculate = (By.ID,'btnCalculate')
save = (By.ID,'btnSave')
repayment = (By.ID,'tvRepayment')
interest = (By.ID,'tvInterestOnly')
class CalculatorPage:
    def __init__(self, driver):
        self.driver = driver

    def get_amount(self):
        return self.driver.find_element(*amount)

    def get_term(self):
        return self.driver.find_element(*term)

    def get_rate(self):
        return self.driver.find_element(*rate)

    def get_calculate(self):
        return self.driver.find_element(*calculate)

    def get_saved(self):
        return self.driver.find_element(*save)

    def get_repayment(self):
        return self.driver.find_element(*repayment)

    def get_interest(self):
        return self.driver.find_element(*interest)