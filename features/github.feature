# Created by Abdul-ur-Rehman at 10/08/2025

  Feature: GitHub API Validation

    @github
    Scenario: Session management check
      Given I have github auth credentials
      When I hit getRepo API of github
      Then status code of response should be 200