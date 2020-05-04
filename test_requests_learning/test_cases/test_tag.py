import json

import jsonpath

from test_requests_learning.api.tag import Tag
from test_requests_learning.api.wework import WeWork


class TestTag:

    # def test_token(self):
    #     self.wework = WeWork()
    #     self.wework.get_token("8erACdo2vg4s7qYWOaEMYwREWG4olWUunenTSXQbraU")
    #

    def test_get(self):
        self.tag = Tag()
        self.tag.get()
        self.tag.params["name"] = "demo3"
        # self.tag.add()
        # a = self.tag.json_path("$..tag[?(@.name=='fff')]")
        # delete_id = a[0]["id"]
        # print(delete_id)
        # self.tag.delete(delete_id)
        # self.tag.get()

