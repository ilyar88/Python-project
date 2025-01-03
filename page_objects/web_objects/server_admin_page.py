from selenium.webdriver.common.by import By

search = (By.CSS_SELECTOR,".css-fcoerl-input-input")
new_user = (By.CSS_SELECTOR,"a[href='admin/users/create']")
users_list = (By.XPATH,"//table[@class='filter-table form-inline filter-table--hover']/tbody/tr")
user_by_name = (By.CSS_SELECTOR,"a[title=' ']")
delete = (By.XPATH,"//span[text()='Delete user']")
confirm_delete = (By.CSS_SELECTOR,"button[aria-label='Confirm Modal Danger Button']")

class ServerAdminPage():
    def __init__(self, driver):
        self.driver = driver

    def get_search(self):
        return self.driver.find_element(*search)

    def get_new_user(self):
        return self.driver.find_element(*new_user)

    def get_users_list(self):
        return self.driver.find_elements(*users_list)

    def get_user_by_index(self, index: int):
        return self.get_users_list()[index]

    def get_by_user_name(self, name: str):
        return self.driver.find_element(user_by_name[0],user_by_name[1].replace(' ',name))

    def get_delete(self):
        return self.driver.find_element(*delete)

    def get_confirm_delete(self):
        return self.driver.find_element(*confirm_delete)