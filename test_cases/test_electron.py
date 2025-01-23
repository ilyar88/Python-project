import allure
import pytest
from extensions.verifications import Verifications
from workflows.electron_flows import ElectronFlows

@pytest.mark.usefixtures('init_electron_driver')
class Test_Electron:
    @allure.title('Test01: add and verify new task')
    @allure.description('This test adds a new task and verifies it in the list')
    def test_add_and_verify_new_task(self):
        ElectronFlows.set_color_flow(['Learn JS'],0)
        Verifications.verify_equals(ElectronFlows.get_number_of_tasks_flow(),1)

    @allure.title('Test02: add and verify new tasks')
    @allure.description('This test adds new tasks and verifies them in the list')
    def test_add_and_verify_new_tasks(self):
        tasks = ['Learn JMeter','Learn AI Driven Test Automation','Learn DevOps']
        ElectronFlows.set_color_flow(tasks,1)
        Verifications.verify_equals(ElectronFlows.get_number_of_tasks_flow(), 3)

    def teardown_method(self):
        ElectronFlows.empty_list_flow()
