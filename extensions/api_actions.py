import allure
import requests
from requests.auth import HTTPBasicAuth
from utilities.common_ops import get_data

bearer_token = get_data('Token')

headers = {
    'Authorization': f'Bearer {bearer_token}',
    'Content-Type': 'application/json'
}

class APIActions:
    @staticmethod
    @allure.step('Get request')
    def get(path, user, password):
        return requests.get(path,headers=headers,auth=HTTPBasicAuth(user,password))

    @staticmethod
    @allure.step('Extract value from response')
    def extract_value_from_response(response, nodes):
        try:
            value = response.json()
            for node in nodes:
                value = value[node]
            return value
        except (KeyError, TypeError, ValueError):
            return None

    @staticmethod
    @allure.step('Post request')
    def post(path,payload, user, password):
        return requests.post(path,json=payload,headers=headers,auth=HTTPBasicAuth(user,password)).status_code

    @staticmethod
    @allure.step('Put request')
    def put(path,payload, user, password):
        return requests.put(path,json=payload,headers=headers,auth=HTTPBasicAuth(user,password)).status_code

    @staticmethod
    @allure.step('Delete request')
    def delete(path, user, password):
        return requests.delete(path,headers=headers,auth=HTTPBasicAuth(user,password)).status_code
