import requests
from pytest_bdd import given, when, then, scenarios
from pytest_bdd.parsers import parse

from Tests.Models.MyGist import MyGist
from Tests.API.utils.GistAPI import GistAPI



scenarios('../Features/GistAPI.feature')

@given(parse('create gist with API'), target_fixture="gist_one_file")
@when(parse('create gist with API'), target_fixture="gist_one_file")
def create_gist(api_session, gist_one_file: MyGist):
    response = GistAPI(api_session).create_gist(gist_one_file)
    assert response.status_code == 201
    gist_one_file.set_id(response.json()["id"])
    print(f"Gist id is {gist_one_file.get_id()}")
    return gist_one_file

@then(parse("gist is created"))
def validate_gist_id(gist_one_file: MyGist):
    assert gist_one_file.get_id() is not None

@when("update gist name with API", target_fixture="response")
def update_gist(api_session, gist_one_file: MyGist):
    gist_one_file.desc = "UPDATED"+gist_one_file.desc
    response = GistAPI(api_session).update_gist(gist_one_file)
    assert response.status_code == 200
    return response

@when("delete gist with API", target_fixture="response")
def update_gist(api_session, gist_one_file: MyGist):
    response = GistAPI(api_session).delete_gist(gist_one_file)
    return response

@then("gist name is updated")
def validate_gist_name(response: requests, gist_one_file: MyGist):
    gist_name = response.json()["description"]
    assert gist_name == gist_one_file.desc

@then("gist is deleted")
def validate_gist_name(response: requests):
    assert response.status_code == 204

