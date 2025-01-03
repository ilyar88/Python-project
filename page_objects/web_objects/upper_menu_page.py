from selenium.webdriver.common.by import By

general = (By.LINK_TEXT, 'General')
home = (By.LINK_TEXT, 'Home')
panel = (By.CSS_SELECTOR, "button[aria-label='Add panel']")
save_dashboard = (By.CSS_SELECTOR, "button[aria-label='Save dashboard']")
dashboard_settings = (By.CSS_SELECTOR, "button[aria-label='Dashboard settings']")
cycle_view = (By.CSS_SELECTOR, "button[aria-label='Cycle view mode']")

class UpperMenuPage:
    def __init__(self, driver):
        self.driver = driver

    def get_general(self):
        return self.driver.find_element(*general)

    def get_home(self):
        return self.driver.find_element(*home)

    def get_panel(self):
        return self.driver.find_element(*panel)

    def get_save_dashboard(self):
        return self.driver.find_element(*save_dashboard)

    def get_dashboard_settings(self):
        return self.driver.find_element(*dashboard_settings)

    def get_cycle_view(self):
        return self.driver.find_element(*cycle_view)