import allure
from extensions.ui_actions import UiActions
import utilities.manage_pages as page

class DesktopFlows:
    @staticmethod
    @allure.step('Calculate equation')
    def calculate_flows(equation):
        for i in equation:
            DesktopFlows.calculator_click(i)
        UiActions.click(page.standard_calc.get_equal())
    @staticmethod
    def calculator_click(value):
        if value == '0':
            UiActions.click(page.standard_calc.get_zero())
        elif value == '1':
            UiActions.click(page.standard_calc.get_one())
        elif value == '2':
            UiActions.click(page.standard_calc.get_two())
        elif value == '3':
            UiActions.click(page.standard_calc.get_three())
        elif value == '4':
            UiActions.click(page.standard_calc.get_four())
        elif value == '5':
            UiActions.click(page.standard_calc.get_five())
        elif value == '6':
            UiActions.click(page.standard_calc.get_six())
        elif value == '7':
            UiActions.click(page.standard_calc.get_seven())
        elif value == '8':
            UiActions.click(page.standard_calc.get_eight())
        elif value == '9':
            UiActions.click(page.standard_calc.get_nine())
        elif value == '+':
            UiActions.click(page.standard_calc.get_plus())
        elif value == '-':
            UiActions.click(page.standard_calc.get_minus())
        elif value == '*':
            UiActions.click(page.standard_calc.get_multi())
        elif value == '/':
            UiActions.click(page.standard_calc.get_divide())
        else:
            raise Exception('Invalid input: ' + value)

    @staticmethod
    @allure.step('Get calculator result')
    def get_result_flows():
        return page.standard_calc.get_result().text.replace("Display is","").strip()

    @staticmethod
    @allure.step('Clear calculator page')
    def clear_flows():
        UiActions.click(page.standard_calc.get_clear())
