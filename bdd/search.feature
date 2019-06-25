Feature: i want to search for products
  Scenario Outline: : Search
    Given i am on home page
    When i search for <term>
    Then i should see list <search_count>

Examples: By category
    |term|search_count|
    |phones|2         |
    |bags  |7         |

Examples: By product name
    |term|search_count|
    |Madison earbuds|3|