import allure
import page_objects.web_objects.main_page as main
import page_objects.web_objects.server_admin_page
from extensions.ui_actions import UiActions
import utilities.manage_pages as page
from extensions.verifications import Verifications
from utilities.common_ops import wait, For, get_data, read_csv

class WebFlows:
    # Static method to log in to Grafana using the provided user credentials
    @staticmethod
    @allure.step('Login to Grafana flow')  # Allure step annotation for reporting
    def login_flow(user: str, password: str):
        # Enter the username and password into the login form
        UiActions.enter_text(page.web_login.get_user_name(), user)
        UiActions.enter_text(page.web_login.get_password(), password)
        # Click the submit button to initiate login
        UiActions.click(page.web_login.get_submit())
        # If a "skip" button appears (e.g., "skip 2FA"), click it
        if page.web_login.get_skip():
            UiActions.click(page.web_login.get_skip()[0])

    # Static method to verify the title of the Grafana homepage
    @staticmethod
    @allure.step('Verify grafana title flow')  # Allure step annotation for reporting
    def verify_grafana_title(expected: str):
        # Wait until the main title element is displayed
        wait(For.ELEMENT_EXISTS, main.main_title)
        # Retrieve the actual title text from the page
        actual = page.web_main.get_main_title().text
        # Verify that the actual title matches the expected title
        Verifications.verify_equals(actual, expected)

    # Static method to verify that the correct menu buttons are displayed using smart assertions
    @staticmethod
    @allure.step('Verify displayed menu button flow using smart assertions')  # Allure step annotation for reporting
    def verify_menu_buttons_smart_assertions():
        # Create a list of menu elements to verify
        elems = [page.web_upper_menu.get_general(),
                 page.web_upper_menu.get_home(),
                 page.web_upper_menu.get_panel(),
                 page.web_upper_menu.get_save_dashboard(),
                 page.web_upper_menu.get_dashboard_settings(),
                 page.web_upper_menu.get_cycle_view()]
        # Use soft assertions to check the presence of each element
        Verifications.soft_assert(elems)

    # Static method to verify the displayed menu buttons using custom assertions
    @staticmethod
    @allure.step('Verify displayed menu button flow using my implementation')  # Allure step annotation for reporting
    def verify_menu_buttons():
        # Create a list of menu elements to verify
        elems = [page.web_upper_menu.get_general(),
                 page.web_upper_menu.get_home(),
                 page.web_upper_menu.get_panel(),
                 page.web_upper_menu.get_save_dashboard(),
                 page.web_upper_menu.get_dashboard_settings(),
                 page.web_upper_menu.get_cycle_view()]
        # Use soft assertions to check the presence of each element
        Verifications.soft_assert(elems)

    # Static method to navigate to the "Users" section under the "Server Admin" menu
    @staticmethod
    @allure.step('Go to users flow')  # Allure step annotation for reporting
    def open_users():
        # Hover over the "Server Admin" menu and click the "Users" option
        elem1 = page.web_left_menu.get_server_admin()
        elem2 = page.web_server_admin_menu.get_users()
        UiActions.mouse_hover(elem1, elem2)

    # Static method to create a new user in the Grafana system
    @staticmethod
    @allure.step('Create new user flow')  # Allure step annotation for reporting
    def create_user(name, email, password):
        # Click the "New User" button to create a new user
        UiActions.click(page.web_server_admin.get_new_user())
        # Fill in the new user's name, email, and password fields
        UiActions.enter_text(page.web_server_admin_new_user.get_name(), name)
        UiActions.enter_text(page.web_server_admin_new_user.get_email(), email)
        UiActions.enter_text(page.web_server_admin_new_user.get_password(), password)
        # Click the "Create User" button to submit the form
        UiActions.click(page.web_server_admin_new_user.get_create_user())

    # Static method to verify the number of users displayed in the users table
    @staticmethod
    @allure.step('Verify number of users in table flow')  # Allure step annotation for reporting
    def verify_number_of_users(number: int):
        # Only verify if the number is greater than 0
        if number > 0:
            # Wait for the users list to be displayed
            wait(For.ELEMENT_DISPLAYED, page_objects.web_objects.server_admin_page.users_list)
            # Verify the number of users in the table
            Verifications.verify_number_of_elements(page.web_server_admin.get_users_list(), number)

    # Static method to search for a user in the users table based on a search value
    @staticmethod
    @allure.step('Search user from users table flow')  # Allure step annotation for reporting
    def search_user(search_value):
        # Enter the search value into the search field
        UiActions.enter_text(page.web_server_admin.get_search(), search_value)

    # Static method to delete a user from the users table based on a search criterion
    @staticmethod
    @allure.step('Delete user from users table flow')  # Allure step annotation for reporting
    def delete_user(by, value):
        # If deleting by username, click the corresponding user row
        if by == 'user':
            UiActions.click(page.web_server_admin.get_by_user_name(value))
        # If deleting by index, click the user row at the specified index
        elif by == 'index':
            UiActions.click(page.web_server_admin.get_user_by_index(value))
        # Click the "Delete" button to initiate the deletion
        UiActions.click(page.web_server_admin.get_delete())
        # Confirm the deletion by clicking the "Confirm Delete" button
        UiActions.click(page.web_server_admin.get_confirm_delete())

    # Static method to navigate to the Grafana home page
    @staticmethod
    @allure.step('Go to home flow')  # Allure step annotation for reporting
    def grafana_home(self):
        # Open the URL specified in the configuration
        self.driver.get(get_data('Url'))

    # Static method to read data from a CSV file and return a list of tuples
    @staticmethod
    def read_csv():
        # Read data from the CSV file specified in the configuration
        data = read_csv(get_data('CSV_Location'))
        # Return a list of tuples where each tuple contains the first and second column from the CSV
        return [(data[i][0], data[i][1]) for i in range(len(data))]


