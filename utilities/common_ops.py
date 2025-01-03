import csv
from datetime import datetime
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import test_cases.conftest as conf
import xml.etree.ElementTree as ET
from enum import Enum


def get_data(node_name):
    root = ET.parse('../configuration/data.xml').getroot()
    return root.find('.//' + node_name).text

def wait(for_element, locator: tuple[By, str]):
    if for_element == For.ELEMENT_EXISTS:
        WebDriverWait(conf.driver, int(get_data('WaitTime'))).until(EC.presence_of_element_located(locator))
    elif for_element == For.ELEMENT_DISPLAYED:
        WebDriverWait(conf.driver, int(get_data('WaitTime'))).until(EC.visibility_of_element_located(locator))

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

class By(str, Enum):
    USER = 'user'
    INDEX = 'index'