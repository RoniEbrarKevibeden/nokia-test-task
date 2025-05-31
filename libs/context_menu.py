# context_menu.py
# Helper class to underline the context menu text using JavaScript
# Written for use in Robot Framework + pytest

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ContextMenu:
    def __init__(self, driver):
        # Store the Selenium WebDriver instance
        self.driver = driver

    def underline_context_menu_text(self):
        """
        This method finds the element that says:
        'Right-click to open Context menu' and underlines it using JavaScript.
        """

        # XPath to find the target element with the specific visible text
        target_xpath = '//*[contains(text(), "Right-click to open Context menu")]'

        # Wait until the element is visible on the page
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, target_xpath))
        )

        # JavaScript code to add underline style to the element
        script = """
        const el = document.evaluate(arguments[0], document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue;
        if (el) el.style.textDecoration = 'underline';
        """

        # Execute the JS with the XPath as argument
        self.driver.execute_script(script, target_xpath)
