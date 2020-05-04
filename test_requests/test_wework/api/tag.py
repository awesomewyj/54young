import requests

from test_requests.test_wework.api.base_api import BaseApi
from test_requests.test_wework.api.wework import WeWork


def api(fun):
    def magic(*args, **kwargs):
        base_api: BaseApi = args[0]

        method=fun.__name__

        base_api.params=kwargs
        req=base_api.api_load("../api/tag.api.yaml")[method]
        return base_api.api_send(req)
        # fun(*args, **kwargs)

    return magic

class Tag(WeWork):
    secret = "8erACdo2vg4s7qYWOaEMYwREWG4olWUunenTSXQbraU"

    def __init__(self):
        self.data = self.api_load("../api/tag.api.yaml")


    def get(self,**kwargs):
        return self.api_send(self.data["get"])

    # def get(self):
    #     url = "https://qyapi.weixin.qq.com/cgi-bin/externalcontact/get_corp_tag_list"
    #     r = requests.post(url = url,
    #                       params={"access_token": self.get_token(self.secret)},
    #                       json={"tag_id":[]})
    #     self.format(r)
    #     return r.json()


    def add(self,name,**kwargs):
        self.params['name'] = name
        ##todo 用装饰器来替换
        return self.api_send(self.data["add"])

    # def add(self,name,**kwargs):
    #     url = "https://qyapi.weixin.qq.com/cgi-bin/externalcontact/add_corp_tag"
    #     r = requests.post(url=url,
    #                       params={"access_token": self.get_token(self.secret)},
    #                       json={"tag": [
    #                           {
    #                               "name":name
    #                           }
    #                       ],
    #                       "group_id":"etBWGXEQAAsl-TY2HsLx_SNSNamziT0w"})
    #     self.format(r)
    #     return r.json()

    def update(self):
        pass

    def delete(self, tag_id=[], group_id=[]):
        self.params['tag_id'] = tag_id
        self.params['group_id'] = group_id
        ##todo 用装饰器来替换
        return self.api_send(self.data["delete"])
    #
    # def delete(self,tag_id=[],group_id=[]):
    #     url = "https://qyapi.weixin.qq.com/cgi-bin/externalcontact/del_corp_tag"
    #     r = requests.post(url=url,
    #                       params={"access_token": self.get_token(self.secret)},
    #                       json={"tag_id": tag_id,
    #                             'group_id':group_id
    #                       })
    #     self.format(r)
    #     return r.json()


    @api
    def xxx(self):
        pass

