*** Settings ***
Library    SeleniumLibrary
Library    ../resources/keywords.py

*** Variables ***
${URL}    https://demos.telerik.com/kendo-react-ui/layout/menu/context-menu/overview/func?theme=default-ocean-blue-a11y
${SCREENSHOT_PATH}    ../screenshots/contextmenu_result.png
${HEADLESS}    True

*** Test Cases ***
KendoReact ContextMenu Styling with Python Keywords
    # Start browser with or without headless mode
    ${options}=    Evaluate    sys.modules['selenium.webdriver'].FirefoxOptions()    sys, selenium.webdriver
    Run Keyword If    '${HEADLESS}'=='True'    Call Method    ${options}    add_argument    -headless
    Create WebDriver    Firefox    options=${options}

    Go To    ${URL}
    Maximize Browser Window
    Sleep    3s

    Apply Underline To Context Text
    Sleep    1s

    Capture Page Screenshot    ${SCREENSHOT_PATH}
    [Teardown]    Close Browser
