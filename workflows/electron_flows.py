from time import sleep
import allure
from selenium.webdriver.common.keys import Keys
import utilities.manage_pages as page
from extensions.ui_actions import UiActions
from extensions.verifications import Verifications
from utilities.common_ops import RGB

class ElectronFlows:
    # Static method to add a new task by entering the task name and simulating 'Enter' key press
    @staticmethod
    @allure.step('Add new task flow')  # Allure step annotation for reporting
    def add_new_task_flow(task_name):
        # Enter the task name in the 'create task' input field
        UiActions.enter_text(page.electron_task.get_create(), task_name)
        # Simulate pressing 'Enter' key to submit the task
        UiActions.enter_text(page.electron_task.get_create(), Keys.RETURN)

    # Static method to get the number of tasks in the task list
    @staticmethod
    @allure.step('Get number of tasks flow')  # Allure step annotation for reporting
    def get_number_of_tasks_flow():
        # Return the count of tasks in the task list
        return len(page.electron_task.get_tasks())

    # Static method to delete all tasks from the task list
    @staticmethod
    @allure.step('Empty task from list flow')  # Allure step annotation for reporting
    def empty_list_flow():
        # Loop through the tasks and delete them one by one
        for x in range(ElectronFlows.get_number_of_tasks_flow()):
            sleep(0.5)  # Adding sleep to allow time for UI actions
            # Hover over the delete button of the first task and delete it
            UiActions.mouse_hover_tooltip(page.electron_task.get_delete_buttons()[0])

    # Static method to select a color for each task in the provided task list
    @staticmethod
    @allure.step('Choose color flow')  # Allure step annotation for reporting
    def choose_color_flow(tasks, offset):
        # Loop through each task in the list and assign a color
        for index, task in enumerate(tasks):
            # Click on the select color arrow to open color options
            UiActions.click(page.electron_task.get_select_arrow())
            # Choose the color corresponding to the task based on the index and offset
            UiActions.click(page.electron_task.get_color()[index + offset])
            # Close the color options dropdown
            UiActions.click(page.electron_task.get_select_arrow())
            # Add the new task to the list
            ElectronFlows.add_new_task_flow(task)
            # Verify that the task has the correct color applied
            ElectronFlows.verify_color_task_flow(list(RGB)[index + offset].value)

    # Static method to verify that the correct color is applied to a task
    @staticmethod
    @allure.step('Set color to task flow')  # Allure step annotation for reporting
    def verify_color_task_flow(color):
        # Loop through all task elements and check their color style
        for elem in page.electron_task.get_task_color():
            # If the color is found in the task's style attribute, verify it
            if color in elem.get_attribute("style"):
                Verifications.verify_string(color, elem.get_attribute("style"))


