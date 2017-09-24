  Feature: Registration

 Scenario: Registration passed
   Given I have access to the system
     And I am on registration page
    When I submit the form with valid patient details
    Then the registration passed

 Scenario: Registration failed
   Given I have access to the system
     And I am on registration page
    When I submit the form with invalid patient details
    Then the registration failed
