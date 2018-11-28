import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

import env

class wait_for_opacity_change(object):
    def __init__(self, locator):
        self.locator = locator

    def __call__(self, driver):
        try:
            element = EC._find_element(driver, self.locator)
            element.value_of_css_property("opacity")
            return element.value_of_css_property("opacity") == 1
        except Exception:
            return False

driver = webdriver.Chrome()
driver.get("https://www.ereaderiq.com/track/drops/asin/")
elem = driver.find_element_by_name("email")
elem.clear()
elem.send_keys(env.email)
elem.send_keys(Keys.RETURN)

with open('extracted_first_links', 'r') as f:
    read_data = f.readlines()

urls = [line.rstrip('\n') for line in read_data if line.startswith('https://www.amazon.com')]

possible_answers = [
    'You were previously tracking this book.',
    "This book has been added to your Watch List.",
    "You are already tracking this book."
]

time.sleep(2)
wait = WebDriverWait(driver, 10)
for url in urls:
    elem = driver.find_element_by_name("asin")
    elem.clear()
    elem.send_keys(url)
    elem.send_keys(Keys.RETURN)
    time.sleep(15)
    # wait.until(wait_for_opacity_change((By.CSS_SELECTOR, 'li.response')))
    # assert any([answer for answer in possible_answers if answer in driver.page_source])
driver.close()