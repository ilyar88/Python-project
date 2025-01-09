import allure
import utilities.manage_pages as page
import test_cases.conftest as conf
from extensions.mobile_actions import MobileActions
from extensions.verifications import Verifications
from utilities.common_ops import get_data
class MobileFlows:
    @staticmethod
    @allure.step('Fill in mortgage details flow')
    def mortgage_flow(amount, term, rate, saved=False):
        MobileActions.enter_text(page.mobile_calculator.get_amount(),amount)
        MobileActions.enter_text(page.mobile_calculator.get_term(), term)
        MobileActions.enter_text(page.mobile_calculator.get_rate(), rate)
        MobileActions.click(page.mobile_calculator.get_calculate())
        if saved:
            MobileActions.click(page.mobile_calculator.get_saved())

    @staticmethod
    @allure.step('Verify repayment flow')
    def verify_mortgage_repayment(expected):
        actual = page.mobile_calculator.get_repayment().text
        Verifications.verify_equals(actual, '£' + expected)

    @staticmethod
    @allure.step('Swipe screen flow')
    def swipe_screen(direction):
        width = conf.mobile_size['width']
        height = conf.mobile_size['height']
        start_x = None
        start_y = None
        end_x = None
        end_y = None
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
        MobileActions.swipe(start_x,start_y,end_x,end_y,int(get_data('Swipe_duration')))

    @staticmethod
    @allure.step('Verify and delete saved transaction flow')
    def verify_rate_delete_transaction(expected):
        actual = page.mobile_saved.get_rate().text
        Verifications.verify_equals(actual,expected + '%')
        MobileActions.tap(page.mobile_saved.get_delete())
        MobileActions.tap(page.mobile_saved.get_confirm_delete())