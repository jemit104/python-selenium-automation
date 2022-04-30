from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path='/Users/svetlanalevinsohn/JobEasy/10-python-selenium-automation/chromedriver')
driver.get('https://www.amazon.com/')

# By ID
driver.find_element(By.ID, 'twotabsearchtextbox')
driver.find_element(By.CSS_SELECTOR, '#twotabsearchtextbox')
driver.find_element(By.CSS_SELECTOR, "input#twotabsearchtextbox")

# By Classes
# 1 class
driver.find_element(By.CSS_SELECTOR, "span.icp-nav-flag-us")
driver.find_element(By.CSS_SELECTOR, ".icp-nav-flag-us")
# by multiple classes
driver.find_element(By.CSS_SELECTOR, "span.icp-nav-flag.icp-nav-flag-us")
driver.find_element(By.CSS_SELECTOR, ".icp-nav-flag.icp-nav-flag-us")

# By other attributes
driver.find_element(By.CSS_SELECTOR, "a[href='/gp/bestsellers/?ref_=nav_cs_bestsellers']")
driver.find_element(By.CSS_SELECTOR, "a[data-csa-c-content-id='nav_cs_bestsellers']")
driver.find_element(By.CSS_SELECTOR, "[data-csa-c-content-id='nav_cs_bestsellers']")  # <- no tag
driver.find_element(By.CSS_SELECTOR, "a[href='/gp/bestsellers/?ref_=nav_cs_bestsellers'][data-csa-c-content-id='nav_cs_bestsellers']")

# By class and attr
driver.find_element(By.CSS_SELECTOR, "a.nav-a[data-csa-c-content-id='nav_cs_bestsellers']")
driver.find_element(By.CSS_SELECTOR, "a[data-csa-c-content-id='nav_cs_bestsellers'].nav-a")
# By id and attr
driver.find_element(By.CSS_SELECTOR, "#twotabsearchtextbox[name='field-keywords']")
# By partial attr
driver.find_element(By.CSS_SELECTOR, "[href*='ap_signin_notification_privacy_notice']")

# By parent and child elements (parent -> child)
driver.find_element(By.CSS_SELECTOR, "#legalTextRow [href*='ap_signin_notification_privacy_notice']")
driver.find_element(By.CSS_SELECTOR, "div.a-section #legalTextRow [href*='ap_signin_notification_privacy_notice']")
driver.find_element(By.CSS_SELECTOR, "div.a-section [href*='ap_signin_notification_privacy_notice']")

