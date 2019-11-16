from behave import *
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from hamcrest import assert_that, equal_to
from selenium.webdriver.support import expected_conditions as EC

# TODO: change background in state.feature to @fixture and before feature combo
@given('the user have tasks to set states')
def step_impl(context):
    elements = context.browser.find_elements_by_xpath('//header/input')
    input_elem = elements[0]
    assert len(elements) > 0
    for i in range(5):
        input_elem.send_keys(context.text + str(i))
        input_elem.send_keys(Keys.ENTER)
    context.input_elem = input_elem


@given('the user has selected active task to set state')
def step_impl(context):
    tasks = context.browser.find_elements_by_xpath("//section/ul/li")
    assert len(tasks) > 0
    context.tasks = []
    for i in tasks:
        if i.get_attribute('class') == context.text.rstrip():
            context.tasks.append(i)
    assert len(context.tasks) > 0


@when('the user clicks on the change state button')
def step_impl(context):
    for i in context.tasks:
        elem = i.find_element_by_xpath('div/input[@class="toggle"]')
        assert EC.element_to_be_clickable(elem)
        elem.click()


@then('task state now is completed')
def step_impl(context):
    for i in context.tasks:
        assert i.get_attribute('class') == "completed"


@then('task state now is Active')
def step_impl(context):
    for i in context.tasks:
        assert i.get_attribute('class') == ""

