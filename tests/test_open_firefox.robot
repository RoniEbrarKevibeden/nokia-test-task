*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${URL}    https://demos.telerik.com/kendo-react-ui/layout/menu/context-menu/overview/func?theme=default-ocean-blue-a11y
${SCREENSHOT_PATH}    ../screenshots/contextmenu_result.png

*** Test Cases ***
KendoReact ContextMenu Styling
    Open Browser    ${URL}    browser=firefox
    Maximize Browser Window
    Sleep    3s

    # Accept cookies if needed
    Run Keyword And Ignore Error    Click Element    xpath=//button[contains(., "Accept Cookies")]
    Sleep    1s

    # Wait for the text to appear directly (no iframe needed)
    Wait Until Page Contains Element    xpath=//*[contains(text(), 'Right-click to open Context menu')]    timeout=15s

    # Underline the target text using JavaScript
    Execute JavaScript
    ...    document.evaluate("//*[contains(text(), 'Right-click to open Context menu')]", document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue.style.textDecoration = 'underline'

    Sleep    1s
    Capture Page Screenshot    ${SCREENSHOT_PATH}

    [Teardown]    Close Browser
