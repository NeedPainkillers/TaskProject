from behave import fixture
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC


@fixture(name="generate.input")
def generate_input(context, *args):
    if context.browser is not None:
        elements = context.browser.find_elements_by_xpath('//header/input')
        if elements is not None:
            input_elem = elements[0]
            for arg in args:
                input_elem.send_keys(arg)
                input_elem.send_keys(Keys.ENTER)


@fixture(name="generate.input.completed")
def generate_input_completed(context, *args):
    generate_input(context, *args)
    if args is not None:
        tasks = context.browser.find_elements_by_xpath("//section/ul/li")[-len(args):]
        for i in tasks:
            elem = i.find_element_by_xpath('div/input[@class="toggle"]')
            if EC.element_to_be_clickable(elem):
                elem.click()


