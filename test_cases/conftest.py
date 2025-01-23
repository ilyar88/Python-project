import os
import allure
import mysql.connector
import pytest
from applitools.selenium import Eyes
from selenium import webdriver
import appium.webdriver
from appium.webdriver.common.multi_action import MultiAction
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.action_chains import ActionChains

#from selenium.webdriver.support.event_firing_webdriver import EventFiringWebDriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
#from utilities.event_listener import EventListener
from utilities.manage_pages import ManagePages
from utilities.common_ops import get_data, get_time_stamp

driver = None
action = None
action2 = None #For using multiple actions
m_action = None
mobile_size = None
db_connector = None
eyes = Eyes()  # Applitools Eyes instance

@pytest.fixture(scope='class')
def init_web_driver(request):
    # Initialize the driver based on the browser setting
    globals()['driver'] = get_web_driver()
    #globals()['driver'] = EventFiringWebDriver(edriver, EventListener())
    driver = globals()['driver']
    driver.maximize_window()
    driver.implicitly_wait(int(get_data('WaitTime')))
    driver.get(get_data('Url'))
    request.cls.driver = driver
    globals()['action'] = ActionChains(driver)
    ManagePages.init_web_pages()
    yield
    driver.quit()
    if get_data('ExecuteApplitools').lower() == 'yes':
        eyes.close()  # Applitools close
        eyes.abort()  # Applitools abort in case of an issue

@pytest.fixture(scope='function')
def current_page(request):
    driver = globals().get('driver', None)
    request.cls.driver = driver
    yield
    driver.quit()

@pytest.fixture(scope='class')
def init_mobile_driver(request):
    globals()['driver'] = get_mobile_driver()
    driver = globals()['driver']
    driver.implicitly_wait(int(get_data('WaitTime')))
    request.cls.driver = driver
    globals()['action'] = TouchAction(driver)
    request.cls.action = globals()['action']
    globals()['action2'] = TouchAction(driver)
    request.cls.action2 = globals()['action2']
    globals()['m_action'] = MultiAction(driver)
    request.cls.m_action = globals()['m_action']
    globals()['mobile_size'] = driver.get_window_size()
    request.cls.mobile_size = globals()['mobile_size']
    ManagePages.init_mobile_pages()
    yield
    driver.quit()

def get_web_driver():
    browser_name = get_data('Browser').lower()
    if browser_name == 'chrome':
        return webdriver.Chrome(ChromeDriverManager().install())
    elif browser_name == 'firefox':
        return webdriver.Firefox(GeckoDriverManager().install())
    elif browser_name == 'edge':
        return webdriver.Edge(EdgeChromiumDriverManager().install())
    else:
        raise ValueError(f"Invalid browser name: '{browser_name}'. Supported: 'Chrome', 'Firefox', 'Edge'.")

def get_mobile_driver():
    device_type = get_data('Mobile_device').lower()
    if device_type == 'android':
        return get_android()
    elif device_type == 'ios':
        return get_ios()
    else:
        raise ValueError(f"Wrong input, unrecognized  mobile OS.")

@pytest.fixture(scope='class')
def init_electron_driver(request):
    globals()['driver'] = get_electron_driver()
    driver = globals()['driver']
    driver.implicitly_wait(int(get_data('WaitTime')))
    request.cls.driver = driver
    globals()['action'] = ActionChains(driver)
    request.cls.action = globals()['action']
    ManagePages.init_electron_pages()
    yield
    driver.quit()

@pytest.fixture(scope='class')
def init_desktop_driver(request):
    globals()['driver'] = get_desktop_driver()
    driver = globals()['driver']
    driver.implicitly_wait(int(get_data('WaitTime')))
    request.cls.driver = driver
    ManagePages.init_desktop_pages()
    yield
    driver.quit()

@pytest.fixture(scope='class')
def init_db_connection(request):
    db_connector = mysql.connector.connect(
        host=get_data('DB_Host'),
        database=get_data('DB_Name'),
        user=get_data('DB_User'),
        password=get_data('DB_Password')
    )
    globals()['db_connector'] = db_connector
    request.cls.db_connector = db_connector
    yield
    db_connector.close()

def get_electron_driver():
    options = webdriver.ChromeOptions()
    options.binary_location = get_data('Electron_App')
    return webdriver.Chrome(chrome_options=options,executable_path=get_data('Electron_Driver'))

def get_desktop_driver():
    dc = {
        'app': get_data('Application_Name'),
        'platformName': 'Windows',
        'deviceName': 'WindowsPC'
    }
    return appium.webdriver.Remote(get_data('WinAppDriver_Service'), dc)
def get_android():
    dc = {
        'udid': get_data('Udid'),
        'appPackage': get_data('App_package'),
        'appActivity': get_data('App_activity'),
        'platformName': 'android'
    }
    return appium.webdriver.Remote(get_data('Appium_server'), dc)

def get_ios():
    dc = {
        'udid': get_data('Udid'),
        'bundle_id': get_data('Bundle_id'),
        'platformName': 'ios'
    }
    return appium.webdriver.Remote(get_data('Appium_server'), dc)

# Catch exceptions and errors to take screenshots on failures
def pytest_exception_interact(node, call, report):
    if report.failed:
        if globals()['driver'] is not None:  # If it is None -> this is an exception from an API test
            test_case_name = node.name.replace(" ", "_")
            folder_path = os.path.join(get_data('ScreenShotPath'), get_time_stamp())
            os.makedirs(folder_path, exist_ok=True)
            image = f"{folder_path}/{test_case_name}.png"
            globals()['driver'].get_screenshot_as_file(image)
            allure.attach.file(image, attachment_type=allure.attachment_type.PNG)
