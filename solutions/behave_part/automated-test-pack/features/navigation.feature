Feature: Navigation

 Scenario Outline: Display navigation menu items
   When I am logged in as "<user type>"
   Then I can see "<menu item>" option on my navigation menu

   Examples:
   | user type | menu item       |
   | doctor    | My patients     |
   | doctor    | My invitations  |
   | patient   | My invitations  |
   | patient   | Invite a doctor |
