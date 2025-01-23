from selenium.webdriver.common.by import By

zero = (By.NAME,"Zero")
one = (By.NAME,"One")
two = (By.NAME,"Two")
three = (By.NAME,"Three")
four = (By.NAME,"Four")
five = (By.NAME,"Five")
six = (By.NAME,"Six")
seven = (By.NAME,"Seven")
eight = (By.NAME,"Eight")
nine = (By.NAME,"Nine")
plus = (By.NAME,"Plus")
minus = (By.NAME,"Minus")
multi = (By.NAME,"Multiply by")
divide = (By.NAME,"Divide by")
equal = (By.NAME,"Equals")
result = (By.XPATH,"//*[@AutomationId='CalculatorResults']")
clear = (By.NAME,"Clear")

class StandardPage:
    def __init__(self,driver):
        self.driver = driver

    def get_zero(self):
        return self.driver.find_element(*zero)

    def get_one(self):
        return self.driver.find_element(*one)

    def get_two(self):
        return self.driver.find_element(*two)

    def get_three(self):
        return self.driver.find_element(*three)

    def get_four(self):
        return self.driver.find_element(*four)

    def get_five(self):
        return self.driver.find_element(*five)

    def get_six(self):
        return self.driver.find_element(*six)

    def get_seven(self):
        return self.driver.find_element(*seven)

    def get_eight(self):
        return self.driver.find_element(*eight)

    def get_nine(self):
        return self.driver.find_element(*nine)

    def get_plus(self):
        return self.driver.find_element(*plus)

    def get_minus(self):
        return self.driver.find_element(*minus)

    def get_multi(self):
        return self.driver.find_element(*multi)

    def get_divide(self):
        return self.driver.find_element(*divide)

    def get_equal(self):
        return self.driver.find_element(*equal)

    def get_result(self):
        return self.driver.find_element(*result)

    def get_clear(self):
        return self.driver.find_element(*clear)
