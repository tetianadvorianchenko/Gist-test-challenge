import pytest
import requests
import uuid

from Tests.Models.MyGist import MyGist


@pytest.fixture(scope="session")
def api_session():
    bearer_token = "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"
    api_url = "https://api.github.com/gists"
    header_accept = "application/vnd.github+json"
    header_github_api_version = "2022-11-28"
    headers = {
        'Accept': header_accept,
        'X-GitHub-Api-Version': header_github_api_version,
        'Authorization': f"Bearer {bearer_token}"
    }
    response = requests.get(api_url, headers=headers)
    assert response.status_code == 200
    session = requests.Session()
    session.headers.update({"Authorization": f"Bearer {bearer_token}"})
    yield session

@pytest.fixture(scope="class")
def gist_one_file():
    my_uuid = uuid.uuid4()
    gist = MyGist(
        f"my test description {my_uuid}",
        {f"file1 name {my_uuid}":{"content":"Hello dear reader, this is file content"}}
    )
    return gist

# set up a hook to be able to check if a test has failed
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    # execute all other hooks to obtain the report object
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)


# check if a test has failed
@pytest.fixture(scope="function", autouse=True)
def test_failed_check(request):
    yield
    # request.node is an "item" because we use the default
    # "function" scope
    if request.node.rep_setup.failed:
        print("setting up a test failed!", request.node.nodeid)
    elif request.node.rep_setup.passed:
        if request.node.rep_call.failed:
            print("executing test failed", request.node.nodeid)
