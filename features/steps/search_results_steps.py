from selenium.webdriver.common.by import By
from behave import given, when, then

SEARCH_RESULT_TEXT = (By.XPATH, "//span[@class='a-color-state a-text-bold']")


@then('Verify search results for {expected_result} are shown')
def verify_search_results(context, expected_result):
    actual_result = context.driver.find_element(*SEARCH_RESULT_TEXT).text
    assert expected_result == actual_result, f'Error! Actual text {actual_result} does not match expected {expected_result}'


