import allure
from extensions.api_actions import APIActions
from utilities.common_ops import get_data

# Retrieving necessary configuration data (URL, Username, Password)
url = get_data('Url')
user = get_data('UserName')
password = get_data('Password')

class APIFlows:
    # Static method to get a value from Grafana API by sending a GET request
    @staticmethod
    @allure.step('Get value from grafana api flow')  # Allure step annotation for reporting
    def get_value_from_api(nodes, name):
        # Send GET request to Grafana API to search for team by name
        response = APIActions.get(url + '/api/teams/search?name=' + name, user, password)
        # Extract value from response using the provided nodes
        return APIActions.extract_value_from_response(response, nodes)

    # Static method to create a new team in Grafana by sending a POST request
    @staticmethod
    @allure.step('Create new team in grafana flow')  # Allure step annotation for reporting
    def create_team(name, email):
        # Construct the payload with the team name and email
        payload = {'name': name, 'email': email}
        # Send POST request to create a new team
        return APIActions.post(url + '/api/teams', payload, user, password)

    # Static method to update an existing team in Grafana by sending a PUT request
    @staticmethod
    @allure.step('Update team in grafana flow')  # Allure step annotation for reporting
    def update_team(name, email, id):
        # Construct the payload with the updated team name and email
        payload = {'name': name, 'email': email}
        # Send PUT request to update the team with the given ID
        return APIActions.put(url + '/api/teams/' + str(id), payload, user, password)

    # Static method to delete a team in Grafana by sending a DELETE request
    @staticmethod
    @allure.step('Delete team in grafana flow')  # Allure step annotation for reporting
    def delete_team(id):
        # Send DELETE request to remove the team with the given ID
        return APIActions.delete(url + '/api/teams/' + str(id), user, password)
