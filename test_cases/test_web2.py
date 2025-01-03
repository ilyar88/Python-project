import time
import pytest
from workflows.web_flows import WebFlows

@pytest.mark.usefixtures('current_page')
class Test_Web:
    def test_verify_upper_menu(self):
        WebFlows.verify_menu_buttons_smart_assertions()
        time.sleep(2)



