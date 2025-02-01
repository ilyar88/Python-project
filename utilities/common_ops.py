import csv
from datetime import datetime
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import test_cases.conftest as conf
import xml.etree.ElementTree as ET
from enum import Enum

##############################################################
# Function Name: get_data
# Function Description: Reads data from an external XML file ('data.xml')
# Function Parameters: string - node(tag) name (the name of the XML node to retrieve data from)
# Function Return: string - the text value of the specified node(tag)
##############################################################
def get_data(node_name):
    # Parse the XML file 'data.xml' and get its root element
    root = ET.parse('configuration/data.xml').getroot()
    # Find and return the text of the specified node(tag) within the XML
    return root.find('.//' + node_name).text

##############################################################
# Function Name: wait
# Function Description: Waits for an element to satisfy a specific condition using Selenium WebDriver
# Function Parameters: 
#   - for_element: the condition to wait for (an enum from the For class)
#   - locator: a tuple specifying the locator method (By) and the value (string) to find the element
# Function Return: None
##############################################################
def wait(for_element, locator: tuple[By, str]):
    # Based on the provided condition, wait for the element to meet the specified condition
    if for_element == For.ELEMENT_EXISTS:
        WebDriverWait(conf.driver, int(get_data('WaitTime'))).until(EC.presence_of_element_located(locator))  # Wait until element exists
    elif for_element == For.ELEMENT_DISPLAYED:
        WebDriverWait(conf.driver, int(get_data('WaitTime'))).until(EC.visibility_of_element_located(locator))  # Wait until element is visible
    elif for_element == For.ELEMENT_CLICKABLE:
        WebDriverWait(conf.driver, int(get_data('WaitTime'))).until(EC.element_to_be_clickable(locator))  # Wait until element is clickable

##############################################################
# Function Name: read_csv
# Function Description: Reads data from a CSV file and stores it in a list
# Function Parameters: file_name (string) - the name of the CSV file to read
# Function Return: list - a list containing the rows of the CSV file
##############################################################
def read_csv(file_name):
    data = []  # Initialize an empty list to store CSV data
    with open(file_name, newline='') as file:
        reader = csv.reader(file)  # Create a CSV reader object
        for row in reader:
            data.insert(len(data), row)  # Insert each row into the list
        return data  # Return the list of rows

##############################################################
# Function Name: get_time_stamp
# Function Description: Generates a timestamp based on the current date and time
# Function Parameters: None
# Function Return: string - the current date and time formatted as a string
##############################################################
def get_time_stamp():
    return datetime.now().strftime("%Y-%m-%d-%H-%M")  # Return the timestamp formatted as Year-Month-Day-Hour-Minute

##############################################################
# Enum for selecting element condition (whether the element exists, is visible, or clickable)
# This Enum is used by the wait method to select which condition to wait for
##############################################################
class For(str, Enum):
    ELEMENT_EXISTS = 'element_exists'  # Wait for element to exist
    ELEMENT_DISPLAYED = 'element_displayed'  # Wait for element to be visible
    ELEMENT_CLICKABLE = 'element_clickable'  # Wait for element to be clickable

##############################################################
# Enum for selecting the method of locating elements (by user or by index)
##############################################################
class By(str, Enum):
    USER = 'user'  # Use user-defined criteria for locating an element
    INDEX = 'index'  # Use an index to locate an element

##############################################################
# Enum for saving mortgage transactions (either Yes or No)
# This Enum can be used for saving or discarding a transaction based on the user's choice
##############################################################
class Saved():
    Yes = True  # Representing a 'Yes' for saving the transaction
    No = False  # Representing a 'No' for not saving the transaction

##############################################################
# Enum for indicating the direction of movement (left, right, up, or down)
# This can be used for any scenario where directional movement is required (e.g., scrolling, dragging)
##############################################################
class Direction(str, Enum):
    LEFT = 'left'  # Move left
    RIGHT = 'right'  # Move right
    DOWN = 'down'  # Move down
    UP = 'up'  # Move up

##############################################################
# Enum for RGB color values, used for consistent color references
# Can be used for verifying elements' color or styling in UI tests
##############################################################
class RGB(str, Enum):
    SALMON_RED = "rgb(255, 103, 93)"  # RGB value for Salmon Red
    ORANGE = "rgb(249, 167, 77)"  # RGB value for Orange
    YELLOW = "rgb(245, 206, 83)"  # RGB value for Yellow
    GREEN = "rgb(114, 204, 87)"  # RGB value for Green
    BLUE = "rgb(87, 185, 244)"  # RGB value for Blue
    PURPLE = "rgb(210, 137, 226)"  # RGB value for Purple
    GRAY = "rgb(165, 165, 167)"  # RGB value for Gray
