*** Settings ***
Library    SeleniumLibrary
Test Setup    Open Browser    http://localhost:3000/    chrome
Test Teardown    Close Browser
*** Test Cases ***
Valid Login
    Input Text    GREET    myusername
    Input Text    NAME=password    mypassword
    
Constants
    Log    Hello
    Log    Hello, world!!

Variables
    Log    ${GREET}
    Log    ${GREET}, ${NAME}!!