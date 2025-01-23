from time import sleep
import allure
from selenium.webdriver.common.keys import Keys
import utilities.manage_pages as page
from extensions.ui_actions import UiActions
from extensions.verifications import Verifications
from utilities.common_ops import RGB

class ElectronFlows:
     @staticmethod
     @allure.step('Add new task flow')
     def add_new_task_flow(task_name):
          UiActions.enter_text(page.electron_task.get_create(),task_name)
          UiActions.enter_text(page.electron_task.get_create(), Keys.RETURN)

     @staticmethod
     @allure.step('Get number of tasks flow')
     def get_number_of_tasks_flow():
          return len(page.electron_task.get_tasks())

     @staticmethod
     @allure.step('Empty task from list flow')
     def empty_list_flow():
          for x in range(ElectronFlows.get_number_of_tasks_flow()):
               sleep(0.5)
               UiActions.mouse_hover_tooltip(page.electron_task.get_delete_buttons()[0])

     @staticmethod
     @allure.step('Choose color flow')
     def choose_color_flow(tasks, offset):
          for index, task in enumerate(tasks):
               UiActions.click(page.electron_task.get_select_arrow())
               UiActions.click(page.electron_task.get_color()[index + offset])
               UiActions.click(page.electron_task.get_select_arrow())
               ElectronFlows.add_new_task_flow(task)
               ElectronFlows.verify_color_task_flow(list(RGB)[index + offset].value)

     @staticmethod
     @allure.step('Set color to task flow')
     def verify_color_task_flow(color):
          for elem in page.electron_task.get_task_color():
               if color in elem.get_attribute("style"):
                    Verifications.verify_string(color,elem.get_attribute("style"))

