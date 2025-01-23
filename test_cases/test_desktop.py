import allure
import pytest
from extensions.verifications import Verifications
from workflows.desktop_flows import DesktopFlows

@pytest.mark.usefixtures('init_desktop_driver')
class Test_Desktop:
    @allure.title('Test01: adding 2 numbers')
    @allure.description('This test adds 2 numbers and verify the result')
    def test_add_numbers_and_verify(self):
        DesktopFlows.calculate_flows('1+7')
        Verifications.verify_equals(DesktopFlows.get_result_flows(),'8')

    @allure.title('Test02: arithmetic actions')
    @allure.description('This test does some arithmetic actions and verify the result')
    def test_arithmetic_actions(self):
        DesktopFlows.calculate_flows('2*5+50/2-25')
        Verifications.verify_equals(DesktopFlows.get_result_flows(), '5')

    @allure.title('Test03: divide by zero')
    @allure.description('This test divide by zero and verify the result')
    def test_divide_by_zero(self):
        DesktopFlows.calculate_flows('0/0')
        Verifications.verify_string('Result is undefined',DesktopFlows.get_result_flows())

    def teardown_method(self):
        DesktopFlows.clear_flows()

