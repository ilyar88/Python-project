import allure
import utilities.manage_pages as page
import test_cases.conftest as conf
from extensions.mobile_actions import MobileActions
from extensions.verifications import Verifications
from utilities.common_ops import get_data

class MobileFlows:
    # Static method to fill in mortgage details, calculate the repayment, and optionally save the transaction
    @staticmethod
    @allure.step('Fill in mortgage details flow')  # Allure step annotation for reporting
    def mortgage_flow(amount, term, rate, saved=False):
        # Enter the mortgage amount in the appropriate field
        MobileActions.enter_text(page.mobile_calculator.get_amount(), amount)
        # Enter the mortgage term in the appropriate field
        MobileActions.enter_text(page.mobile_calculator.get_term(), term)
        # Enter the mortgage rate in the appropriate field
        MobileActions.enter_text(page.mobile_calculator.get_rate(), rate)
        # Click the "Calculate" button to compute the mortgage repayment
        MobileActions.click(page.mobile_calculator.get_calculate())
        # If the "saved" flag is True, save the transaction
        if saved:
            MobileActions.click(page.mobile_calculator.get_saved())

    # Static method to verify the mortgage repayment value against an expected value
    @staticmethod
    @allure.step('Verify repayment flow')  # Allure step annotation for reporting
    def verify_mortgage_repayment(expected):
        # Get the actual repayment value displayed on the screen
        actual = page.mobile_calculator.get_repayment().text
        # Verify if the actual repayment matches the expected repayment value
        Verifications.verify_equals(actual, '£' + expected)

    # Static method to swipe the mobile screen in the specified direction (left, right, up, down)
    @staticmethod
    @allure.step('Swipe screen flow')  # Allure step annotation for reporting
    def swipe_screen(direction):
        # Retrieve the mobile screen's width and height from configuration
        width = conf.mobile_size['width']
        height = conf.mobile_size['height']
        # Initialize swipe start and end coordinates
        start_x = None
        start_y = None
        end_x = None
        end_y = None

        # Determine the swipe direction and calculate the start and end coordinates based on the screen size
        if direction == 'left':
            start_x = width * 0.9
            end_x = width * 0.1
            start_y = end_y = height * 0.5
        elif direction == 'right':
            start_x = width * 0.1
            end_x = width * 0.9
            start_y = end_y = height * 0.5
        elif direction == 'up':
            start_y = height * 0.9
            end_y = height * 0.1
            start_x = end_x = width * 0.5
        elif direction == 'down':
            start_y = height * 0.1
            end_y = height * 0.9
            start_x = end_x = width * 0.5
        
        # Perform the swipe action with the calculated coordinates and duration
        MobileActions.swipe(start_x, start_y, end_x, end_y, int(get_data('Swipe_duration')))

    # Static method to verify the saved mortgage rate and delete the saved transaction
    @staticmethod
    @allure.step('Verify and delete saved transaction flow')  # Allure step annotation for reporting
    def verify_rate_delete_transaction(expected):
        # Get the actual saved mortgage rate
        actual = page.mobile_saved.get_rate().text
        # Verify if the actual rate matches the expected rate
        Verifications.verify_equals(actual, expected + '%')
        # Tap the delete button for the saved transaction
        MobileActions.tap(page.mobile_saved.get_delete())
        # Confirm the deletion by tapping the confirmation button
        MobileActions.tap(page.mobile_saved.get_confirm_delete())
