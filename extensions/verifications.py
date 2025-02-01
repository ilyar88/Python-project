import allure
from selenium.webdriver.remote.webelement import WebElement
from smart_assertions import soft_assert, verify_expectations

class Verifications:
    """
    A utility class containing various verification methods for assertions in tests.
    """

    @staticmethod
    @allure.step('Verify equals')
    def verify_equals(actual, expected):
        """
        Verifies if the actual value equals the expected value.
        Raises an assertion error if the values are not equal.
        
        :param actual: The actual value.
        :param expected: The expected value.
        """
        assert actual == expected, 'Verify equals failed: ' + str(actual) + ' is not equal to: ' + str(expected)

    @staticmethod
    @allure.step('Verify string in string')
    def verify_string(actual, expected):
        """
        Verifies if the actual string is a substring of the expected string.
        Raises an assertion error if the actual string is not found in the expected string.
        
        :param actual: The string to search for.
        :param expected: The string in which to search.
        """
        assert actual in expected, 'Verify equals failed: ' + str(actual) + ' is not in: ' + str(expected)

    @staticmethod
    @allure.step('Verify element is displayed')
    def is_displayed(elem: WebElement):
        """
        Verifies if a web element is displayed on the page.
        Raises an assertion error if the element is not displayed.
        
        :param elem: The web element to check.
        """
        assert elem.is_displayed(), 'Verify is displayed failed, element: ' + elem.text + ' is not displayed'

    @staticmethod
    @allure.step('Soft verification (assert) of elements using smart assertions')
    def soft_assert(elems):
        """
        Performs soft assertions on a list of web elements to check if they are displayed.
        Uses the `smart_assertions` library for soft assertions, allowing the test to continue 
        even if some elements are not displayed. Verifies all expectations at the end.
        
        :param elems: List of web elements to verify.
        """
        for i in range(len(elems)):
            soft_assert(elems[i].is_displayed())
        verify_expectations()

    @staticmethod
    @allure.step('Soft verification (assert) of elements using my implementation')
    def soft_displayed(elems):
        """
        Custom implementation of soft assertions for checking if elements are displayed.
        Collects all elements that fail the visibility check and prints their aria-labels. 
        Raises an assertion error if any elements are not displayed.
        
        :param elems: List of web elements to verify.
        """
        failed_elems = []
        for i in range(len(elems)):
            if not elems[i].is_displayed():
                failed_elems.insert(len(failed_elems), elems[i].get_attribute('aria-label'))
        
        if len(failed_elems) > 0:
            for failed_elem in failed_elems:
                print('Soft displayed failed, elements which have failed ' + str(failed_elem))
            raise AssertionError('Soft displayed failed')

    @staticmethod
    @allure.step('Verify number of elements in list')
    def verify_number_of_elements(elems, size):
        """
        Verifies if the number of elements in a list matches the expected size.
        Raises an assertion error if the sizes do not match.
        
        :param elems: List of elements.
        :param size: The expected number of elements.
        """
        assert len(elems) == size, 'Number of elements in list: ' + str(len(elems)) + ' does not match expected: ' + str(size)
