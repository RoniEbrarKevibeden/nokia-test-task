# dropdown.py
# Helper class to handle dropdown interactions (like theme selection)
# Written for use with Robot Framework + pytest unit tests

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class DropdownElement:
    def __init__(self, driver):
        # Receive WebDriver instance from Robot Framework or test
        self.driver = driver

    def change_theme(self, theme_text):
        """
        Selects a theme (e.g., 'Material') from the theme dropdown.
        This uses explicit waits to make sure the elements are interactable.
        """

        # Step 1: Find the theme dropdown (usually says "Default") and click it
        theme_button_xpath = '//span[contains(text(), "Default")]'
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, theme_button_xpath))
        ).click()

        # Step 2: After dropdown opens, click on the desired theme option (like "Material")
        theme_option_xpath = f'//li[contains(text(), "{theme_text}")]'
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, theme_option_xpath))
        ).click()
