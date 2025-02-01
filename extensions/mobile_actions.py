import allure
from extensions.ui_actions import UiActions
import test_cases.conftest as conf

class MobileActions(UiActions):
    @staticmethod
    @allure.step('Tap on element')
    def tap(elem, times=1):
        """
        Simulates a tap action on a mobile element.

        Args:
            elem: The element to tap on.
            times (int): The number of times to tap on the element. Default is 1.
        
        Returns:
            None
        """
        conf.action.tap(elem, times).perform()

    @staticmethod
    @allure.step('Swipe screen')
    def swipe(start_x, start_y, end_x, end_y, duration):
        """
        Simulates a swipe action on the mobile screen.

        Args:
            start_x (int): The starting x-coordinate of the swipe.
            start_y (int): The starting y-coordinate of the swipe.
            end_x (int): The ending x-coordinate of the swipe.
            end_y (int): The ending y-coordinate of the swipe.
            duration (int): The duration of the swipe in milliseconds.
        
        Returns:
            None
        """
        conf.driver.swipe(start_x, start_y, end_x, end_y, duration)

    @staticmethod
    @allure.step('Zoom on element')
    def zoom(element, pixels=200):
        """
        Simulates a zoom gesture on a mobile element by moving two touch points away from each other.

        Args:
            element: The element to zoom on.
            pixels (int): The number of pixels to move apart for the zoom action. Default is 200.
        
        Returns:
            None
        """
        action1 = conf.action  # First touch action
        action2 = conf.action2  # Second touch action
        m_action = conf.m_action  # Multi-touch action
        
        # Get the element's location
        x_loc = element.rect['x']
        y_loc = element.rect['y']
        
        # Define the zoom gesture
        action1.long_press(x=x_loc, y=y_loc).move_to(x=x_loc, y=y_loc + pixels).wait(500).release()
        action2.long_press(x=x_loc, y=y_loc).move_to(x=x_loc, y=y_loc - pixels).wait(500).release()
        
        # Perform the multi-touch zoom action
        m_action.add(action1, action2)
        m_action.perform()

    @staticmethod
    @allure.step('Pinch on element')
    def pinch(element, pixels=200):
        """
        Simulates a pinch gesture on a mobile element by moving two touch points toward each other.

        Args:
            element: The element to pinch on.
            pixels (int): The number of pixels to move inward for the pinch action. Default is 200.
        
        Returns:
            None
        """
        action1 = conf.action  # First touch action
        action2 = conf.action2  # Second touch action
        m_action = conf.m_action  # Multi-touch action
        
        # Get the element's location
        x_loc = element.rect['x']
        y_loc = element.rect['y']
        
        # Define the pinch gesture
        action1.long_press(x=x_loc, y=y_loc + pixels).move_to(x=x_loc, y=y_loc).wait(500).release()
        action2.long_press(x=x_loc, y=y_loc - pixels).move_to(x=x_loc, y=y_loc).wait(500).release()
        
        # Perform the multi-touch pinch action
        m_action.add(action1, action2)
        m_action.perform()
