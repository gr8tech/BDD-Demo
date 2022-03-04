from behave import given, when, then, fixture, use_fixture

from selenium.webdriver import Safari, ActionChains
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By

import platform


@given('user navigates to "formula1.com"')
def step_impl(context):
    if platform.system() == 'Darwin':
        context.driver = Safari()
    else:
        context.driver = Chrome()  # put chrome driver in the path
    context.driver.get('https://www.formula1.com')
    context.driver.maximize_window()
    trust = context.driver.find_element(by=By.CSS_SELECTOR, value='#truste-consent-button')
    if trust:
        trust.click()
    assert 'F1' in context.driver.title


@when('user hovers over the "Teams"')
def step_impl(context):
    team_link = context.driver.find_element(by=By.XPATH, value='//*[@id="primaryNav"]/div/div[2]/ul/li[6]/a/span')
    ActionChains(context.driver).move_to_element(team_link).perform()
    for y in range(10):
        ActionChains(context.driver).move_by_offset(1, y).perform()


@then('all the 10 Teams are listed')
def step_impl(context):
    teams = context.driver.find_elements(by=By.XPATH,
                                         value='//div[@class="nav-list teams"]//span[@class="name f1--xs"]')
    for team in teams:
        assert team.get_attribute("innerText") in ['Alfa Romeo', 'AlphaTauri', 'Alpine', 'Aston Martin', 'Ferrari',
                                                   'Haas', 'McLaren', 'Mercedes', 'Red Bull', 'Williams']
    context.driver.quit()
