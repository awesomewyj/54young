from test_requests_learning.api.wework import WeWork


class Tag(WeWork):

    def __init__(self):
        secret = "8erACdo2vg4s7qYWOaEMYwREWG4olWUunenTSXQbraU"
        self.params["access_token"] = self.get_token(secret)
        self.tag_data = self.yaml_load("../api/tag.yaml")


    def get(self):

        self.api_send(self.tag_data["get"])

    def add(self):
        self.api_send(self.tag_data["add"])

    def delete(self, tag_id=[], group_id=[]):
        self.params['tag_id'] = tag_id
        self.params['group_id'] = group_id
        ##todo 用装饰器来替换
        return self.api_send(self.tag_data["delete"])
