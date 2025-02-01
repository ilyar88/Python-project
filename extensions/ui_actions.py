import allure
import test_cases.conftest as conf
from selenium.webdriver.remote.webelement import WebElement

class UiActions:
    @staticmethod
    @allure.step('Click on element')
    def click(elem: WebElement):
        """
        Clicks on a given web element.

        Args:
            elem (WebElement): The web element to be clicked.

        Returns:
            None
        """
        elem.click()

    @staticmethod
    @allure.step('Enter text')
    def enter_text(elem: WebElement, value: str):
        """
        Clears the text field and enters a specified value into the web element.

        Args:
            elem (WebElement): The text input field web element.
            value (str): The string to be entered in the text field.

        Returns:
            None
        """
        elem.clear()  # Clear any existing text in the field
        elem.send_keys(value)  # Input the new text value

    @staticmethod
    @allure.step('Mouse hover two elements')
    def mouse_hover(elem1: WebElement, elem2: WebElement):
        """
        Performs a mouse hover action over two elements sequentially and clicks on the second element.

        Args:
            elem1 (WebElement): The first web element to hover over.
            elem2 (WebElement): The second web element to hover over and click.

        Returns:
            None
        """
        # Create an ActionChain, move the mouse to elem1, then to elem2, and perform a click.
        conf.ActionChains(conf.driver).move_to_element(elem1).move_to_element(elem2).click().perform()

    @staticmethod
    @allure.step('Right click on element')
    def right_click(elem: WebElement):
        """
        Performs a right-click (context click) on a given web element.

        Args:
            elem (WebElement): The web element to right-click on.

        Returns:
            None
        """
        # Create an ActionChain to perform a context (right) click on the specified element.
        conf.ActionChains(conf.driver).context_click(elem).perform()

    @staticmethod
    @allure.step('Drag and drop')
    def drag_and_drop(elem1: WebElement, elem2: WebElement):
        """
        Drags a web element (source) and drops it onto another web element (target).

        Args:
            elem1 (WebElement): The source web element to be dragged.
            elem2 (WebElement): The target web element where the source element will be dropped.

        Returns:
            None
        """
        # Create an ActionChain to drag elem1 and drop it onto elem2.
        conf.ActionChains(conf.driver).drag_and_drop(elem1, elem2).perform()
