Feature: Testing formula1.com website
  Scenario: All teams listed
     Given user navigates to "formula1.com"
      When user hovers over the "Teams"
      Then all the 10 Teams are listed