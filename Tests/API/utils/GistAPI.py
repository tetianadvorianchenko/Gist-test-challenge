import requests
from requests import Session

from Tests.Models import MyGist


class GistAPI():
    def __init__(self, my_session: Session):
        self.session = my_session
        self.api_url = "https://api.github.com/gists"

    def get_public_gists(self) -> requests:
        return self.session.get("/gists/public")

    def get_gist(self, url="") -> requests:
        return self.session.get(url)

    def create_gist(self, gist):
        return self.session.post(self.api_url, json=gist.build_payload())

    def delete_gist(self, gist: MyGist):
        return self.session.delete(url=f"{self.api_url}/{gist.get_id()}")

    def update_gist(self, gist: MyGist):
        response = self.session.patch(url=f"{self.api_url}/{gist.get_id()}", json=gist.build_payload())
        return response
