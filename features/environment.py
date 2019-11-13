from selenium import webdriver


def before_all(context):
    driver = webdriver.Chrome()
    context.browser = driver


def after_all(context):
    context.browser.quit()
