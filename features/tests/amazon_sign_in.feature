# Created by svetlanalevinsohn at 2/27/22
Feature: Amazon Sign In tests

  Scenario: Sign In page can be opened from SignIn popup
    Given Open Amazon page
    When Click on button from SignIn popup
    Then Verify Sign In page is opened

  Scenario: SignIn popup is visible for a few seconds in the main page
    Given Open Amazon page
    Then SignIn popup is present
    When Wait for 5 seconds
    Then SignIn popup is present
    Then SignIn popup disappears
