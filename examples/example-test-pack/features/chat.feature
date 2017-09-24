Feature: Chat

  Scenario: Sending the message
    Given I am logged in as doctor
      And I have a patient assigned to me
      And I am on patent card details page
     When I type the message in chat window
     Then the message has been sent
