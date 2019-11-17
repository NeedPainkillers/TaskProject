from behave import *
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from hamcrest import assert_that, equal_to


@when('clicks on enter')
def step_impl(context):
    context.input_elem.send_keys(Keys.ENTER)

# input feature start here
@given('the user provided input')
def step_impl(context):
    elements = context.browser.find_elements_by_xpath('//header/input')
    assert  len(elements) > 0
    elements[0].send_keys(context.text)
    context.sended_keys = context.text.rstrip()
    context.input_elem = elements[0]


@then('task added to todos')
def step_impl(context):
    assert_that(context.browser.find_elements_by_xpath('//section/ul/li')[-1].find_elements_by_xpath('div/label')[0].text, equal_to(context.sended_keys))
# input feature ends here


# update feature starts here
@given('the user have task to update')
def step_impl(context):
    elements = context.browser.find_elements_by_xpath('//header/input')
    assert len(elements) > 0
    elements[0].send_keys(context.text)
    context.input_elem = elements[0]


@given('the user has text "{sometext}"')
def step_impl(context, sometext):
    context.new_text = sometext


@when('the user chose the task to update')
def step_impl(context):
    list = context.browser.find_elements_by_xpath('//section/ul/li')
    assert len(list) > 0
    context.task = list[-1]


@when('the user double clicks on task')
def step_impl(context):
    action_chains = ActionChains(context.browser)
    action_chains.double_click(context.task).perform()


@when('the user provided input')
def step_impl(context):
    # getting element what we need to edit
    edit_field = context.task.find_element_by_xpath('input')
    # clear old text
    edit_field.send_keys(Keys.CONTROL, 'a')
    edit_field.send_keys(Keys.BACKSPACE)

    edit_field.send_keys(context.new_text)
    context.input_elem = edit_field


@then('user sees updated task')
def step_impl(context):
    assert_that(context.browser.find_elements_by_xpath('//section/ul/li')[-1].find_elements_by_xpath('div/label')[0].text, equal_to(context.new_text))
# update feature ends here
