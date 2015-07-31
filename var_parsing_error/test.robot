*** Settings ***
Resource          res1.robot
Resource          res2.robot

*** Variables ***
${VAR}            ${VAR1}${VAR2}

*** Test Cases ***
test
    Log    ${VAR}
