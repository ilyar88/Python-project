import allure
from selenium.webdriver.remote.webelement import WebElement
from smart_assertions import soft_assert, verify_expectations


class Verifications:
    @staticmethod
    @allure.step('Verify equals')
    def verify_equals(actual, expected):
        assert actual == expected, 'Verify equals failed: ' + str(actual) + ' is not equals to: ' + str(expected)

    @staticmethod
    @allure.step('Verify element is displayed')
    def is_displayed(elem: WebElement):
        assert elem.is_displayed(), 'Verify is displayed failed, element: ' + elem.text + ' is not displayed'

    @staticmethod
    @allure.step('Soft verification (assert) of elements using smart assertions')
    def soft_assert(elems):
        for i in range(len(elems)):
            soft_assert(elems[i].is_displayed())
        verify_expectations()

    @staticmethod
    @allure.step('Soft verification (assert) of elements using my implementation')
    def soft_displayed(elems):
        failed_elems = []
        for i in range(len(elems)):
            if not elems[i].is_displayed():
                failed_elems.insert(len(failed_elems),elems[i].get_attribute('aria-label'))
        if len(failed_elems) > 0:
            for failed_elem in failed_elems:
                print('Soft displayed failed, elements which have failed ' + str(failed_elem))
            raise AssertionError('Soft displayed failed')

    @staticmethod
    @allure.step('Verify number of elements in list')
    def verify_number_of_elements(elems, size):
        assert len(elems) == size, 'Number of elements in list: ' + str(len(elems)) + ' does not match expected: ' + str(size)