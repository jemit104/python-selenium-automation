from selenium.webdriver.common.by import By
from behave import given, when, then


SEARCH_INPUT = (By.ID, 'twotabsearchtextbox')
SEARCH_BTN = (By.ID, 'nav-search-submit-button')


@given('Open Amazon page')
def open_amazon(context):
    context.driver.get('https://www.amazon.com/')


@when('Search for {search_word}')
def search_amazon(context, search_word):
    context.driver.find_element(*SEARCH_INPUT).send_keys(search_word)
    context.driver.find_element(*SEARCH_BTN).click()

