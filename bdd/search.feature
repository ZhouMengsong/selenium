Feature: i want to search for products
  Scenario Outline: Search
    Given i am on login page
    When i input username <username>
    When i input password <password>
    When i will click submit <password>
    Then i should see notice <error>

Examples: By category
    |username|password|error|
    |zhou1234|zhou1234|0|
    |test1234|zhou1234|1|
    |ecshop|zhou1234|2|
    |ecshop|123456|3|
