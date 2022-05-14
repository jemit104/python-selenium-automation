from behave import given, when, then, step
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


@then('Verify Sign In page is opened')
def verify_sign_in_opened(context):
    context.driver.wait.until(
        EC.url_contains('https://www.amazon.com/ap/signin'),
        message='Sign in page never opened'
    )
