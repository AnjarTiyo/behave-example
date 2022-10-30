Feature: Search Alterra on Search Engine
  As an user
  I want to search "Alterra"
  on Google
  and on DuckDuckGo
  In order to look information of "Alterra"

  Scenario: Seach Alterra on Google
    Given I go to Google.com
    When I type Alterra on Google search bar
    And I hit Google Search button
    Then I should have information regarding "Alterra"

  Scenario: Seach Alterra on DuckDuckGo
    Given I go to DuckDuckGo.com
    When I type Alterra on DuckDuckGo search bar
    And I hit DuckDuckGo Search button
    Then I should have information regarding "Alterra"