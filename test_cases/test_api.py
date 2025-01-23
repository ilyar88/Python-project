import allure
from extensions.verifications import Verifications
from workflows.api_flows import APIFlows

team_name = 'Ilya'
team_email = 'irahmilevich@gmail.com'

class Test_API:
    @allure.title('Test01: create team & verify statis code')
    @allure.description('This test creates new team in grafana')
    def test_create_and_verify_team(self):
        actual = APIFlows.create_team(team_name,team_email)
        Verifications.verify_equals(actual,200)

    @allure.title('Test02: verify team name')
    @allure.description('This test verifies the grafana team member name')
    def test_verify_team_member(self):
        nodes = ['teams',0,'name']
        actual = APIFlows.get_value_from_api(nodes,team_name)
        Verifications.verify_equals(actual, team_name)

    @allure.title('Test03: update team & verify status code')
    @allure.description('This test update team & verify status code')
    def test_update_and_verify_team_name(self):
        nodes = ['teams',0,'id']
        id = APIFlows.get_value_from_api(nodes,team_name)
        actual = APIFlows.update_team(team_name + ' Rahmilevich',team_email,id)
        Verifications.verify_equals(actual, 200)

    @allure.title('Test04: update team name')
    @allure.description('This test verify team member name')
    def test_verify_name_updated_name(self):
        nodes = ['teams',0,'name']
        actual = APIFlows.get_value_from_api(nodes,team_name + ' Rahmilevich')
        Verifications.verify_equals(actual, team_name + ' Rahmilevich')

    @allure.title('Test05: delete team & verify status code')
    @allure.description('This test delete team and verify status code')
    def test_delete_and_verify_team_name(self):
        nodes = ['teams', 0, 'id']
        id = APIFlows.get_value_from_api(nodes,team_name + ' Rahmilevich')
        actual = APIFlows.delete_team(id)
        print(actual)
        Verifications.verify_equals(actual,200)
