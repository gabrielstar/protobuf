from pytest_bdd import scenarios
from pytest_bdd import then, when

scenarios("../features")


@then("I am at Projects Grid page")
def at_projects_grid_page(projects_grid_page):
    assert projects_grid_page.is_at_page()


@when("I click through menus")
def i_click_through_menus(projects_grid_page):
    projects_grid_page.click_menus()
