from behave import use_fixture
from fixtures import generate_input, generate_input_completed
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException


def before_all(context):
    driver = webdriver.Chrome()
    driver.get("http://todomvc.com/examples/react/#/")
    delay = 3
    xpath = '/html/body/section/div/header/input'
    try:
        WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, xpath)))
    except TimeoutException:
        print("Loading took too much time!")
    context.browser = driver


def before_tag(context, tag):
    if tag == "fixture.generate.input":
        use_fixture(generate_input, context, "sample input", "another sample input", "some other sample input")
    if tag == "fixture.generate.input.completed":
        use_fixture(generate_input_completed, context, "sample completed input", "another completed sample input", "some completed other sample input")


def after_all(context):
    context.browser.quit()
    pass
