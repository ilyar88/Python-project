from selenium.webdriver.support.events import EventFiringWebDriver, AbstractEventListener

# Custom event listener class that extends Selenium's AbstractEventListener
class EventListener(AbstractEventListener):
    button_text = None  # A class variable to store the text of a button

    # Called before navigating to a URL
    def before_navigate_to(self, url, driver):
        print("Before Navigating to", url)  # Print the URL before navigating to it

    # Called after navigating to a URL
    def after_navigate_to(self, url, driver):
        print("After Navigating to", url)  # Print the URL after navigating to it

    # Called before navigating back in the browser
    def before_navigate_back(self, driver):
        print("Before Navigating Back", driver.current_url)  # Print the current URL before navigating back

    # Called after navigating back in the browser
    def after_navigate_back(self, driver):
        print("After Navigating Back", driver.current_url)  # Print the current URL after navigating back

    # Called before navigating forward in the browser
    def before_navigate_forward(self, driver):
        print("Before Navigating Forward", driver.current_url)  # Print the current URL before navigating forward

    # Called after navigating forward in the browser
    def after_navigate_forward(self, driver):
        print("After Navigating Forward", driver.current_url)  # Print the current URL after navigating forward

    # Called before locating an element
    def before_find(self, by, value, driver):
        print("Before Find Element:", value)  # Print the value of the element being located

    # Called after locating an element
    def after_find(self, by, value, driver):
        print("After Find Element", value)  # Print the value of the element that was located

    # Called before changing the value of an element (e.g., input fields)
    def before_change_value_of(self, element, driver):
        if element.tag_name == "input":
            print("Before Change Value ", element.get_attribute("value"))  # Print the current value of the input field
        else:
            print("Before Change Value ", element.text)  # Print the current text of the element if not an input field

    # Called after changing the value of an element
    def after_change_value_of(self, element, driver):
        if element.tag_name == "input":
            print("After Change Value ", element.get_attribute("value"))  # Print the new value of the input field
        else:
            print("After Change Value ", element.text)  # Print the new text of the element if not an input field

    # Called before clicking an element
    def before_click(self, element, driver):
        # Store the value of the element before clicking, particularly for button elements
        EventListener.button_text = element.get_attribute("value")  
        if element.tag_name == "input":
            print("Before Click ", EventListener.button_text)  # Print the value of the button/input element
        else:
            print("Before Click ", EventListener.button_text)  # Print the value of the non-input element

    # Called after clicking an element
    def after_click(self, element, driver):
        print("After Click ", EventListener.button_text)  # Print the text of the button after it has been clicked

    # Called before executing a JavaScript script
    def before_execute_script(self, script, driver):
        print("Before Execute Script ", script)  # Print the script that is about to be executed

    # Called after executing a JavaScript script
    def after_execute_script(self, script, driver):
        print("After Execute Script ", script)  # Print the script that has just been executed

    # Called before closing a tab
    def before_close(self, driver):
        print("Before Closing Tab")  # Print a message before closing the tab

    # Called after closing a tab
    def after_close(self, driver):
        print("After Closing Tab")  # Print a message after the tab is closed

    # Called before quitting the browser session
    def before_quit(self, driver):
        print("Before Quiting Session")  # Print a message before quitting the session

    # Called after quitting the browser session
    def after_quit(self, driver):
        print("After Quiting Session")  # Print a message after quitting the session

    # Called when an exception occurs during a test execution
    def on_exception(self, exception, driver):
        print("On Exception: ", exception)  # Print the exception message
