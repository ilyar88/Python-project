import csv
from datetime import datetime
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import test_cases.conftest as conf
import xml.etree.ElementTree as ET
from enum import Enum

##############################################################
# Function ame: get_data
# Function description: this function reads data from external file
# Function parameters: string - node(tag) name
# Function return: string - node(tag) value
##############################################################
def get_data(node_name):
    root = ET.parse('configuration/data.xml').getroot()
    return root.find('.//' + node_name).text

def wait(for_element, locator: tuple[By, str]):
    if for_element == For.ELEMENT_EXISTS:
        WebDriverWait(conf.driver, int(get_data('WaitTime'))).until(EC.presence_of_element_located(locator))
    elif for_element == For.ELEMENT_DISPLAYED:
        WebDriverWait(conf.driver, int(get_data('WaitTime'))).until(EC.visibility_of_element_located(locator))
    elif for_element == For.ELEMENT_CLICKABLE:
        WebDriverWait(conf.driver, int(get_data('WaitTime'))).until(EC.element_to_be_clickable(locator))

def read_csv(file_name):
    data = []
    with open(file_name, newline='') as file:
        reader = csv.reader(file)
        for row in reader:
            data.insert(len(data),row)
        return data

def get_time_stamp():
    return datetime.now().strftime("%Y-%m-%d-%H-%M")

#Enum for selecting displayed element or exist element, my wait method uses this enum
class For(str, Enum):
    ELEMENT_EXISTS = 'element_exists'
    ELEMENT_DISPLAYED = 'element_displayed'
    ELEMENT_CLICKABLE = 'element_clickable'

class By(str, Enum):
    USER = 'user'
    INDEX = 'index'

#Enum for saving mortgage transaction or not
class Saved():
    Yes = True
    No = False

class Direction(str, Enum):
    LEFT = 'left'
    RIGHT = 'right'
    DOWN = 'down'
    UP = 'up'

class RGB(str, Enum):
    SALMON_RED = "rgb(255, 103, 93)"
    ORANGE = "rgb(249, 167, 77)"
    YELLOW = "rgb(245, 206, 83)"
    GREEN = "rgb(114, 204, 87)"
    BLUE = "rgb(87, 185, 244)"
    PURPLE = "rgb(210, 137, 226)"
    GRAY = "rgb(165, 165, 167)"
