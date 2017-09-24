Feature: Login
 Scenario: Login success
   Given I have access to the system
     And I am on the login page
    When I submit the form with valid user credentials
    Then I am redirected to landing page

  Scenario: Login failed
   Given I have access to the system
     And I am on the login page
    When I submit the form with invalid user credentials
    Then I get error message
