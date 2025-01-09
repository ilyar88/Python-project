import allure
import test_cases.conftest as conf
from selenium.webdriver.remote.webelement import WebElement

class UiActions:
    @staticmethod
    @allure.step('Click on element')
    def click(elem: WebElement):
        elem.click()

    @staticmethod
    @allure.step('Enter text')
    def enter_text(elem: WebElement, value: str):
        elem.clear()
        elem.send_keys(value)

    @staticmethod
    @allure.step('Mouse hover two elements')
    def mouse_hover(elem1: WebElement, elem2: WebElement):
        conf.ActionChains(conf.driver).move_to_element(elem1).move_to_element(elem2).click().perform()

    @staticmethod
    @allure.step('Right click on element')
    def right_click(elem: WebElement):
        conf.ActionChains(conf.driver).context_click(elem).perform()

    @staticmethod
    @allure.step('Drag and drop')
    def drag_and_drop(elem1: WebElement, elem2: WebElement):
        conf.ActionChains(conf.driver).drag_and_drop(elem1, elem2).perform()