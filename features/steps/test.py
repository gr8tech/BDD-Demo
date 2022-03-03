from behave import given, when, then, fixture, use_fixture

from selenium.webdriver import Safari
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By


@given(u'driver has launched')
def step_impl(context):
    pass


@when(u'we browse to teams url')
def step_impl(context):
    driver = Safari()
    found_teams = []
    driver.get('https://www.formula1.com/en/teams.html')
    driver.implicitly_wait(10)
    trust = driver.find_element(by=By.CSS_SELECTOR, value='#truste-consent-button')
    if trust:
        trust.click()
    teams = driver.find_elements(by=By.CSS_SELECTOR, value='.listing-info .name ')
    for team in teams:
        found_teams.append(team.text.strip())
    context.teams = ','.join(sorted(found_teams))
    driver.quit()

@then(
    u'available teams are "{teams}"')
def step_impl(context, teams):
    assert(context.teams, teams)
