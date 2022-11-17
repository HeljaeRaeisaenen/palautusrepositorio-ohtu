*** Settings ***
Resource  resource.robot
Test Setup  Input New Command

*** Test Cases ***
Register With Valid Username And Password
    Input Credentials  kalle  kalle123
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
    Input Credentials  kalle  kalle123
    Input New Command
    Input Credentials  kalle  32112345
    Output Should Contain  User with username kalle already exists

Register With Too Short Username And Valid Password
    Input Credentials  a  12345678
    Output Should Contain  Username must be over 3 chars and contain only the letters a-z

Register With Valid Username And Too Short Password
    Input Credentials  mikko  123
    Output Should Contain  Password must be at least 8 chars and contain at least 1 special character or number

Register With Valid Username And Long Enough Password Containing Only Letters
    Input Credentials  mikko  abcdefgh
    Output Should Contain  Password must be at least 8 chars and contain at least 1 special character or number
