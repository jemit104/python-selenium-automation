from selenium.webdriver.common.by import By
from behave import given, when, then, step


SEARCH_INPUT = (By.ID, 'twotabsearchtextbox')
SEARCH_BTN = (By.ID, 'nav-search-submit-button')
HAM_MENU_BTN = (By.ID, 'nav-hamburger-menu')
FOOTER_LINKS = (By.CSS_SELECTOR, 'td.navFooterDescItem a')


@given('Open Amazon page')
def open_amazon(context):
    context.driver.get('https://www.amazon.com/')


@when('Search for {search_word}')
def search_amazon(context, search_word):
    context.driver.find_element(*SEARCH_INPUT).send_keys(search_word)
    context.driver.find_element(*SEARCH_BTN).click()


@then('Verify hamburger menu btn present')
def verify_ham_menu(context):
    context.driver.find_element(*HAM_MENU_BTN)


@then('Verify there are {expected_amount} footer links')
def verify_footer_links_count(context, expected_amount):
    expected_amount = int(expected_amount)  # '38' => 38

    footer_links = context.driver.find_elements(*FOOTER_LINKS)  # [Webelement1, Webelement2, ..]

    assert len(footer_links) == expected_amount, f'Expected {expected_amount} links, but got {len(footer_links)}'
