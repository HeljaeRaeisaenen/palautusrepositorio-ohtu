*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Register Page

*** Test Cases ***
Register With Valid Username And Password
    Set Username  mikko
    Set Password  mikko123
    Set Password Confirmation  mikko123
    Submit Registration
    Register Should Succeed

Register With Too Short Username And Valid Password
    Set Username  mi
    Set Password  mikko123
    Set Password Confirmation  mikko123
    Submit Registration
    Register Should Fail With Message  Username must be at least 3 chars and contain only the letters a-z

Register With Valid Username And Too Short Password
    Set Username  jaakko
    Set Password  89
    Set Password Confirmation  89
    Submit Registration
    Register Should Fail With Message  Password must be at least 8 chars and contain at least 1 special character or number

Register With Nonmatching Password And Password Confirmation
    Set Username  jaakko
    Set Password  jaakko890
    Set Password Confirmation  jaakko899
    Submit Registration
    Register Should Fail With Message  Passwords don't match

Login After Successful Registration
    Set Username  jaakko
    Set Password  jaakko890
    Set Password Confirmation  jaakko890
    Submit Registration
    Go To Login Page
    Login User  jaakko  jaakko890
    Login Should Succeed

Login After Failed Registration
    Set Username  pekka
    Set Password  pekka
    Set Password Confirmation  pekka
    Submit Registration
    Go To Login Page
    Login User  pekka  pekka
    Login Should Fail With Message  Invalid username or password

*** Keywords ***
Register Should Succeed
    Welcome Page Should Be Open

Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}

Submit Registration
    Click Button  Register

Set Password Confirmation
    [Arguments]  ${password}
    Input Password  password_confirmation  ${password}

Login User
    [Arguments]  ${username}  ${password}
    Set Username  ${username}
    Set Password  ${password}
    Submit Credentials
