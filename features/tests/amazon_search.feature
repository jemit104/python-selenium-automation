# Created by svetlanalevinsohn at 4/23/22
Feature: Tests for Amazon search

  Scenario Outline: Verify that user can search for products
    Given Open Amazon page
    When Search for <search_word>
    Then Verify search results for <search_result> are shown
    Examples:
    |search_word  |search_result  |
    |table        |"table"        |
    |dress        |"dress"        |
    |spoons       |"spoons"       |


  Scenario: User sees ham menu btn on the main page
    Given Open Amazon page
    Then Verify hamburger menu btn present

  Scenario: User sees correct amount of footer links
    Given Open Amazon page
    Then Verify there are 38 footer links

  Scenario: Verify that user can see product names and images
    Given Open Amazon page
    When Search for coffee
    Then Verify that every product has a name and an image
