import allure
import pytest
from workflows.web_flows import WebFlows
from utilities.common_ops import get_data, By
import test_cases.conftest as conf

@pytest.mark.usefixtures('init_web_driver')
class Test_Web:
    @allure.title('Test01: verify login Grafana')
    @allure.description('This test verifies a successful login to Grafana')
    def test_verify_login(self):
        WebFlows.login_flow(get_data('UserName'), get_data('Password'))
        WebFlows.verify_grafana_title('Welcome to Grafana')

    @allure.title('Test02: verify upper menu buttons')
    @allure.description('This test verifies upper menu buttons are displayed')
    def test_verify_upper_menu(self):
        WebFlows.verify_menu_buttons_smart_assertions() #sort assertions
        #WebFlows.verify_menu_buttons()

    @allure.title('Test03: verify new user')
    @allure.description('This test creates and verifies a new user')
    def test_verify_new_user(self):
        WebFlows.open_users()
        WebFlows.create_user('Ilya','irahmilevich@gmail.com','Welcome!37')
        WebFlows.create_user('Moshe', 'Moshe@gmail.com', 'Welcome!36')
        WebFlows.verify_number_of_users(5)

    @allure.title('Test04: delete user')
    @allure.description('This test verifies delete users')
    def test_verify_delete_user(self):
        WebFlows.open_users()
        WebFlows.delete_user(By.USER,'Moshe')
        WebFlows.delete_user(By.USER,'Ilya')
        WebFlows.verify_number_of_users(3)

    @allure.title('Test05: filtering users')
    @allure.description('This test filtering users')
    @pytest.mark.parametrize('search_value,expected_users',WebFlows.read_csv())
    def test_user_filtering(self,search_value,expected_users):
        WebFlows.open_users()
        WebFlows.search_user(search_value)
        WebFlows.verify_number_of_users(int(expected_users))

    @allure.title('Test06: visual testing')
    @allure.description('This test verifies visually users table')
    @pytest.mark.skipif(get_data('ExecuteApplitools').lower() == 'no',reason='Run this test only selenium 3.141.0 $ appuim 1.3.0')
    def test_visual_verify_deleted_user(self):
        conf.eyes.api_key = get_data('Applitools_key')  # Set Applitools API key
        conf.eyes.open(conf.driver,'Grafana testing user table','Verify Deleted User')
        WebFlows.open_users()
        conf.eyes.check_window('Users table')
    def teardown_method(self):
        WebFlows.grafana_home(self)
