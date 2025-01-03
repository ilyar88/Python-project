import allure
import page_objects.web_objects.main_page as main
import page_objects.web_objects.server_admin_page
from extensions.ui_actions import UIActions
import utilities.manage_pages as page
from extensions.verifications import Verifications
from utilities.common_ops import wait, For, get_data, read_csv
class WebFlows:
    @staticmethod
    @allure.step('Login to Grafana flow')
    def login_flow(user: str, password: str):
        UIActions.enter_text(page.web_login.get_user_name(), user)
        UIActions.enter_text(page.web_login.get_password(), password)
        UIActions.click(page.web_login.get_submit())
        if page.web_login.get_skip():
            UIActions.click(page.web_login.get_skip()[0])

    @staticmethod
    @allure.step('Verify grafana title flow')
    def verify_grafana_title(expected: str):
        wait(For.ELEMENT_EXISTS, main.main_title)
        actual = page.web_main.get_main_title().text
        Verifications.verify_equals(actual, expected)

    #Verify menu buttons flow using smart assertions
    @staticmethod
    @allure.step('Verify displayed menu button flow using smart assertions')
    def verify_menu_buttons_smart_assertions():
        elems = [page.web_upper_menu.get_general(),
                 page.web_upper_menu.get_home(),
                 page.web_upper_menu.get_panel(),
                 page.web_upper_menu.get_save_dashboard(),
                 page.web_upper_menu.get_dashboard_settings(),
                 page.web_upper_menu.get_cycle_view()]
        Verifications.soft_assert(elems)

    # Verify menu buttons flow using my implementation
    @staticmethod
    @allure.step('Verify displayed menu button flow using my implementation')
    def verify_menu_buttons():
        elems = [page.web_upper_menu.get_general(),
                 page.web_upper_menu.get_home(),
                 page.web_upper_menu.get_panel(),
                 page.web_upper_menu.get_save_dashboard(),
                 page.web_upper_menu.get_dashboard_settings(),
                 page.web_upper_menu.get_cycle_view()]
        Verifications.soft_assert(elems)

    @staticmethod
    @allure.step('Go to users flow')
    def open_users():
        elem1 = page.web_left_menu.get_server_admin()
        elem2 = page.web_server_admin_menu.get_users()
        UIActions.mouse_hover(elem1, elem2)

    @staticmethod
    @allure.step('Create new user flow')
    def create_user(name, email, password):
        UIActions.click(page.web_server_admin.get_new_user())
        UIActions.enter_text(page.web_server_admin_new_user.get_name(),name)
        UIActions.enter_text(page.web_server_admin_new_user.get_email(), email)
        UIActions.enter_text(page.web_server_admin_new_user.get_password(), password)
        UIActions.click(page.web_server_admin_new_user.get_create_user())

    @staticmethod
    @allure.step('Verify number of users in table flow')
    def verify_number_of_users(number: int):
        if number > 0:
            wait(For.ELEMENT_DISPLAYED,page_objects.web_objects.server_admin_page.users_list)
            Verifications.verify_number_of_elements(page.web_server_admin.get_users_list(),number)

    @staticmethod
    @allure.step('Search user from users table flow')
    def search_user(search_value):
        UIActions.enter_text(page.web_server_admin.get_search(),search_value)
    @staticmethod
    @allure.step('Delete user from users table flow')
    def delete_user(by, value):
        if by == 'user':
            UIActions.click(page.web_server_admin.get_by_user_name(value))
        elif by == 'index':
            UIActions.click(page.web_server_admin.get_user_by_index(value))
        UIActions.click(page.web_server_admin.get_delete())
        UIActions.click(page.web_server_admin.get_confirm_delete())

    @staticmethod
    @allure.step('Go to home flow')
    def grafana_home(self):
        self.driver.get(get_data('Url'))

    @staticmethod
    def read_csv():
        data = read_csv(get_data('CSV_Location'))
        return [(data[i][0], data[i][1]) for i in range(len(data))]

