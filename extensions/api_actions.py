import allure
import requests
from requests.auth import HTTPBasicAuth
from utilities.common_ops import get_data

# Retrieve the bearer token from the external data.xml
bearer_token = get_data('Token')

# Define the headers for API requests, including authorization and content type
headers = {
    'Authorization': f'Bearer {bearer_token}',
    'Content-Type': 'application/json'
}

class APIActions:
    @staticmethod
    @allure.step('Get request')
    def get(path, user, password):
        """
        Sends a GET request to the specified path with basic authentication.
        
        Args:
            path (str): The URL endpoint for the GET request.
            user (str): The username for basic authentication.
            password (str): The password for basic authentication.
        
        Returns:
            Response: The response object from the GET request.
        """
        return requests.get(path, headers=headers, auth=HTTPBasicAuth(user, password))

    @staticmethod
    @allure.step('Extract value from response')
    def extract_value_from_response(response, nodes):
        """
        Extracts a specific value from a JSON response based on a list of node keys.
        
        Args:
            response (Response): The response object containing JSON data.
            nodes (list): A list of keys representing the path to the desired value.
        
        Returns:
            Any: The extracted value, or None if the key path is invalid.
        """
        try:
            value = response.json()
            for node in nodes:
                value = value[node]
            return value
        except (KeyError, TypeError, ValueError):
            return None

    @staticmethod
    @allure.step('Post request')
    def post(path, payload, user, password):
        """
        Sends a POST request to the specified path with a JSON payload and basic authentication.
        
        Args:
            path (str): The URL endpoint for the POST request.
            payload (dict): The JSON payload to be sent in the POST request.
            user (str): The username for basic authentication.
            password (str): The password for basic authentication.
        
        Returns:
            int: The HTTP status code from the POST request.
        """
        return requests.post(path, json=payload, headers=headers, auth=HTTPBasicAuth(user, password)).status_code

    @staticmethod
    @allure.step('Put request')
    def put(path, payload, user, password):
        """
        Sends a PUT request to the specified path with a JSON payload and basic authentication.
        
        Args:
            path (str): The URL endpoint for the PUT request.
            payload (dict): The JSON payload to be sent in the PUT request.
            user (str): The username for basic authentication.
            password (str): The password for basic authentication.
        
        Returns:
            int: The HTTP status code from the PUT request.
        """
        return requests.put(path, json=payload, headers=headers, auth=HTTPBasicAuth(user, password)).status_code

    @staticmethod
    @allure.step('Delete request')
    def delete(path, user, password):
        """
        Sends a DELETE request to the specified path with basic authentication.
        
        Args:
            path (str): The URL endpoint for the DELETE request.
            user (str): The username for basic authentication.
            password (str): The password for basic authentication.
        
        Returns:
            int: The HTTP status code from the DELETE request.
        """
        return requests.delete(path, headers=headers, auth=HTTPBasicAuth(user, password)).status_code
