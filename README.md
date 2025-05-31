# Nokia Automation Task - IT Internship

## Description

This project is part of a student internship assignment, focused on automation testing using **Robot Framework**, **Python**, and **Selenium**.  
It automates a UI test for the KendoReact Context Menu component.

---

## Task Summary

- Visit the KendoReact Context Menu demo page.
- Change the theme to **Material**.
- Underline the text: `Right-click to open Context menu` using JavaScript.
- Take a screenshot after applying the styling.

---

## Technologies Used

- Robot Framework
- SeleniumLibrary
- Python (with `unittest.mock`)
- Pytest (for unit testing)

---

## How to Run the Tests

### Robot Framework Test – Task 1

To run the full end-to-end UI automation tests:

```bash
python -m robot tests/test_open_firefox.robot
python -m robot tests/test_with_keywords.robot
