from selenium.webdriver.common.by import By

users = (By.CSS_SELECTOR,"a[href='/admin/users']")
orgs = (By.CSS_SELECTOR,"a[href='/admin/orgs']")
settings = (By.CSS_SELECTOR,"a[href='/admin/settings']")
plugins = (By.CSS_SELECTOR,"a[href='/admin/plugins']")
stats = (By.CSS_SELECTOR,"a[href='/admin/upgrading']")


class ServerAdminMenuPage():
    def __init__(self, driver):
        self.driver = driver

    def get_users(self):
        return self.driver.find_element(*users)

    def get_orgs(self):
        return self.driver.find_element(*orgs)

    def get_settings(self):
        return self.driver.find_element(*settings)

    def get_plugins(self):
        return self.driver.find_element(*plugins)

    def get_stats(self):
        return self.driver.find_element(*stats)