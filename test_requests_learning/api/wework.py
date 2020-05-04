from test_requests_learning.api.BaseApi import BaseApi


class WeWork(BaseApi):

    def get_token(self,secret):

        wework_data = self.yaml_load("../api/wework.yaml")


        self.params['corpsecret'] = secret

        r = self.api_send(wework_data["get_access_token"])
        print(r["access_token"])
        return r["access_token"]







