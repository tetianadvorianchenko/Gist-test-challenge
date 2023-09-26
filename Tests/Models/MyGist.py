import json


class MyGist:
    def __init__(self, description: str = None, files: dict = None, id: str = None) -> object:
        self.desc = description
        self.files = files
        self.gist_id = id

    def set_id(self, gist_id: str):
        self.gist_id = gist_id

    def get_id(self):
        return self.gist_id

    def build_payload(self) -> dict:
        payload = {'description': self.desc, 'files': self.files}
        return payload
