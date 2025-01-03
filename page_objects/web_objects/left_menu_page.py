from selenium.webdriver.common.by import By

grafana = (By.CSS_SELECTOR,"a[aria-label='Home']")
search_dashboards = (By.CSS_SELECTOR,"a[aria-label='Search dashboards']")
create = (By.CSS_SELECTOR,"a[aria-label='Create']")
dashboards = (By.CSS_SELECTOR,"a[aria-label='Dashboards']")
explore = (By.CSS_SELECTOR,"a[aria-label='Explore']")
alerting = (By.CSS_SELECTOR,"a[aria-label='Alerting']")
configuration = (By.CSS_SELECTOR,"a[aria-label='Configuration']")
server_admin = (By.CSS_SELECTOR,"a[aria-label='Server Admin']")
admin = (By.CSS_SELECTOR,"a[aria-label='admin']")
help = (By.CSS_SELECTOR,"a[aria-label='Help']")

class LeftMainPage():
    def __init__(self, driver):
        self.driver = driver

    def get_grafana(self):
        return self.driver.find_element(*grafana)

    def get_search_dashboards(self):
        return self.driver.find_element(*search_dashboards)

    def get_dashboards(self):
        return self.driver.find_element(*dashboards)

    def get_explore(self):
        return self.driver.find_element(*explore)

    def get_alerting(self):
        return self.driver.find_element(*alerting)

    def get_configuration(self):
        return self.driver.find_element(*configuration)

    def get_server_admin(self):
        return self.driver.find_element(*server_admin)

    def get_admin(self):
        return self.driver.find_element(*admin)

    def get_help(self):
        return self.driver.find_element(*help)