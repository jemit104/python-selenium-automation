from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# init driver
driver = webdriver.Chrome()
driver.maximize_window()

# It will be applied to wait.until
# It will check for condition to be met every 500 ms
driver.wait = WebDriverWait(driver, timeout=10)

# Always applied to all find_element commands
# Checks for an element every 100 ms
# No Such Element Ex
driver.implicitly_wait(5)

# open the url
driver.get('https://www.google.com/')

search = driver.find_element(By.NAME, 'q')
search.clear()
search.send_keys('Car')

# wait for 4 sec
# sleep(4)
driver.wait.until(EC.element_to_be_clickable((By.NAME, 'btnK')), message='Search btn not clickable')

# click search
driver.find_element(By.NAME, 'btnK').click()

# verify
assert 'car' in driver.current_url.lower(), f"Expected query not in {driver.current_url.lower()}"
print('Test Passed')

driver.quit()
