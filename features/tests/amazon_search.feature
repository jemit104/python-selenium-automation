# Created by svetlanalevinsohn at 4/23/22
Feature: Tests for Amazon search

  Scenario: Verify that user can search for coffee
    Given Open Amazon page
    When Search for table
    Then Verify search results for "table" are shown

  Scenario: Verify that user can search for dress
    Given Open Amazon page
    When Search for dress
    Then Verify search results for "dress" are shown

