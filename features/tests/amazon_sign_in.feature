# Created by svetlanalevinsohn at 2/27/22
Feature: Amazon Sign In tests

  Scenario: Sign In page can be opened from SignIn popup
    Given Open Amazon page
    When Click on button from SignIn popup
    Then Verify Sign In page is opened
