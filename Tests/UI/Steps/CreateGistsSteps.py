from pytest_bdd import given, when, then, parsers, scenarios
from pytest_bdd.parsers import parse

from Tests.Models.MyGist import MyGist
from Tests.UI.Pages.CreatedGistPage import CreatedGistPage
from Tests.UI.Pages.LoginPage import LoginPage
from Tests.UI.Pages.NewGistPage import NewGistPage

TEST_DATA_DIR = "Tests/TestFiles"

scenarios('../Features/CreateGists.feature')


@given(parsers.parse('user is signed in with {my_login} and {password}'))
def login(init_driver, my_login: str, password: str):
    login_page = LoginPage(init_driver)
    login_page.open_page()
    login_page.wait_for_page()
    login_page.user_login(my_login, password)


@given(parse("open new gist page"), target_fixture="new_gist_page")
def open_new_gist_page(init_driver):
    new_gist_page = NewGistPage(init_driver)
    new_gist_page.open_page()
    new_gist_page.wait_for_page()
    return new_gist_page


@when(parsers.parse('enter the gist description {descr}'), target_fixture="my_gist")
def enter_gist_descr(new_gist_page: NewGistPage, descr: str):
    new_gist_page.get_description().send_keys(descr)
    my_gist = MyGist(description=descr)
    return my_gist


@when(parsers.parse('fill the file name with {value}'))
def enter_gist_descr(new_gist_page: NewGistPage, value: str):
    file_item = new_gist_page.get_file_item()
    new_gist_page.get_file_name(file_item).send_keys(value)


@when(parsers.parse('fill the file content from {file_name} file'), target_fixture="my_gist")
def enter_gist_descr(new_gist_page: NewGistPage, my_gist: MyGist, file_name: str):
    with open(f"{TEST_DATA_DIR}/{file_name}") as f:
        content = f.readlines()
        file_item = new_gist_page.get_file_item()
        new_gist_page.get_file_content(file_item).send_keys(content)
        files = {file_name: content}
        my_gist.files = files
        return my_gist


@when(parsers.parse('create gist with type {gist_type}'))
def create_gist_by_type(new_gist_page: NewGistPage, gist_type: str):
    new_gist_page.get_type_dropdown().click()
    new_gist_page.get_type(f"Create {gist_type}").click()
    new_gist_page.get_element_by_css(new_gist_page.gist_submit_button_css).click()


@then(parse('gist is created'))
def validate_gist(init_driver, my_gist: MyGist):
    created_gist_page = CreatedGistPage(init_driver)
    created_gist_page.wait_for_page()
    assert created_gist_page.get_gist_descr() == my_gist.desc
