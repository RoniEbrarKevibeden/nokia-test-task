# Custom keywords written for Robot Framework
# This script is created by a student for automation practice purposes
# It interacts with a demo site: changes theme and underlines text

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from robot.api.deco import keyword
from robot.libraries.BuiltIn import BuiltIn

# This class handles dropdown interaction (theme selector)
class DropdownElement:
    def __init__(self, driver):
        self.driver = driver

    def select_material_theme(self):
        # Wait until the dropdown is visible and clickable
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//span[contains(@class, "k-dropdown-wrap")]'))
        )
        dropdown = self.driver.find_element(By.XPATH, '//span[contains(@class, "k-dropdown-wrap")]')
        dropdown.click()

        # Wait for the option to appear and click it
        WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((By.XPATH, '//li[contains(text(), "Material") or contains(text(), "Main")]'))
        )
        option = self.driver.find_element(By.XPATH, '//li[contains(text(), "Material") or contains(text(), "Main")]')
        option.click()

# This class handles styling the target text
class ContextMenu:
    def __init__(self, driver):
        self.driver = driver

    def underline_text(self):
        # Use JavaScript to underline the target context menu text
        xpath = "//*[contains(text(), 'Right-click to open Context menu')]"
        script = (
            "document.evaluate(\"" + xpath + "\", document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null)"
            ".singleNodeValue.style.textDecoration = 'underline';"
        )
        self.driver.execute_script(script)

# Define custom Robot Framework keywords using function decorators
@keyword("Change Theme To Material Main")
def change_theme_to_material_main():
    seleniumlib = BuiltIn().get_library_instance('SeleniumLibrary')
    driver = seleniumlib.driver
    dropdown = DropdownElement(driver)
    dropdown.select_material_theme()

@keyword("Apply Underline To Context Text")
def apply_underline_to_context_text():
    seleniumlib = BuiltIn().get_library_instance('SeleniumLibrary')
    driver = seleniumlib.driver
    context = ContextMenu(driver)
    context.underline_text()
