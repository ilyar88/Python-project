import allure
from extensions.api_actions import APIActions
from utilities.common_ops import get_data

url = get_data('Url')
user = get_data('UserName')
password = get_data('Password')

class APIFlows:
    @staticmethod
    @allure.step('Get value from grafana api flow')
    def get_value_from_api(nodes,name):
        response = APIActions.get(url + '/api/teams/search?name=' + name,user,password)
        return APIActions.extract_value_from_response(response,nodes)

    @staticmethod
    @allure.step('Create new team in grafana flow')
    def create_team(name,email):
        payload = {'name': name,'email': email}
        return APIActions.post(url + '/api/teams', payload, user, password)

    @staticmethod
    @allure.step('Update team in grafana flow')
    def update_team(name,email,id):
        payload = {'name': name,'email': email}
        return APIActions.put(url + '/api/teams/' + str(id), payload, user, password)

    @staticmethod
    @allure.step('Delete team in grafana flow')
    def delete_team(id):
        return APIActions.delete(url + '/api/teams/' + str(id), user, password)
