from selenium.webdriver.common.by import By

create = (By.CSS_SELECTOR,"input[placeholder='Create a task']")
tasks = (By.CLASS_NAME,"view_2Ow90")
delete_buttons = (By.CSS_SELECTOR, "svg[class='destroy_19w1q']")
select_arrow = (By.CSS_SELECTOR, "svg[class='downArrowIcon_3Zu5N']")
colors = (By.CSS_SELECTOR, "span[class='tag_21fhY']")
task_colors = (By.CSS_SELECTOR, "span[class='tag_3u4he']")

class TaskPage:
    def __init__(self,driver):
        self.driver = driver

    def get_create(self):
        return self.driver.find_element(*create)
    def get_tasks(self):
        return self.driver.find_elements(*tasks)

    def get_delete_buttons(self):
        return self.driver.find_elements(*delete_buttons)

    def get_select_arrow(self):
        return self.driver.find_element(*select_arrow)

    def get_color(self):
        return self.driver.find_elements(*colors)

    def get_task_color(self):
        return self.driver.find_elements(*task_colors)
