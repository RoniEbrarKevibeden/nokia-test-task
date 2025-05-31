# test_keywords.py
# Unit tests for DropdownElement and ContextMenu helper classes
# These tests use mocking to simulate browser behavior without opening a real browser
# Written by a student as part of an automation testing assignment

import pytest
from unittest.mock import MagicMock, patch
from libs.dropdown import DropdownElement
from libs.context_menu import ContextMenu

# Test case for theme change functionality
def test_change_theme():
    # Create a fake WebDriver object
    driver = MagicMock()

    # Create fake elements to represent dropdown and the theme option
    dropdown_el = MagicMock()
    theme_option = MagicMock()

    # Patch WebDriverWait so that .until() returns our fake elements
    with patch("libs.dropdown.WebDriverWait") as wait_mock:
        wait_instance = wait_mock.return_value
        wait_instance.until.side_effect = [dropdown_el, theme_option]

        # Create instance of the class and call the method
        dropdown = DropdownElement(driver)
        dropdown.change_theme("Material")

        # Verify that the dropdown and option were both clicked
        dropdown_el.click.assert_called_once()
        theme_option.click.assert_called_once()

# Test case for underlining the context menu text
def test_underline_context_menu_text():
    # Create a mock WebDriver
    driver = MagicMock()

    # Patch WebDriverWait to simulate element being found
    with patch("libs.context_menu.WebDriverWait") as wait_mock:
        wait_instance = wait_mock.return_value
        wait_instance.until.return_value = True  # simulate visibility

        # Create object and run the underline function
        context = ContextMenu(driver)
        context.underline_context_menu_text()

        # Check if JavaScript was executed
        driver.execute_script.assert_called_once()

        # Make sure it tried to apply "underline"
        assert "underline" in driver.execute_script.call_args[0][0]
