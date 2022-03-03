@fixture.driver.safari
Feature: Testing formula1.com website

  Scenario: All teams listed
     Given driver has launched
      When we browse to teams url
      Then available teams are "{Alfa Romeo,AlphaTauri,Alpine,Aston Martin,Ferrari,Haas F1 Team,McLaren,Mercedes,Red Bull Racing,Williams}"
