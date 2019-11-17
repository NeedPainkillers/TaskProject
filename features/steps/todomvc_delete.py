from behave import *
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC


@given('the user chose task to delete')
def step_impl(context):
    tasks = context.browser.find_elements_by_xpath("//section/ul/li")
    assert len(tasks) > 0
    context.tasks = tasks


@when('the user hovered cursor over chosen task and clicks on delete crest')
def step_impl(context):
    for task in context.tasks:
        hover = ActionChains(context.browser).move_to_element(task)
        hover.perform()
        delete_button = task.find_element_by_xpath('div/button[@class="destroy"]')
        assert EC.element_to_be_clickable(delete_button)
        delete_button.click()


@then('task deleted from list')
def step_impl(context):
    assert len(context.browser.find_elements_by_xpath("//section/ul/li")) == 0


@given('the user have completed tasks')
def step_impl(context):
    tasks = context.browser.find_elements_by_xpath("//section/ul/li")
    assert len(tasks) > 0
    context.tasks = []
    for i in tasks:
        if i.get_attribute('class') == "":
            context.tasks.append(i)


@when('the user clicks on delete all completed button')
def step_impl(context):
    # /html/body/section/div/footer/button
    buttons = context.browser.find_elements_by_xpath('//footer/button[@class="clear-completed"]')
    assert len(buttons) > 0
    clear_all = buttons[0]
    assert EC.element_to_be_clickable(clear_all)
    clear_all.click()


@then('all completed tasks are deleted from list')
def step_impl(context):
    tasks = context.browser.find_elements_by_xpath("//section/ul/li")
    completed_tasks = []
    for i in tasks:
        if i.get_attribute('class') == "":
            completed_tasks.append(i)
    assert len(completed_tasks) == 0
