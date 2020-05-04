import json

import requests

from test_requests.test_wework.api.wework import WeWork


class GroupChat(WeWork):
    # secret = "XyfLGZNUTJDvAMKbbd_LtavLAZx-7WR28hlvylK21Xk"
    secret = "8erACdo2vg4s7qYWOaEMYwREWG4olWUunenTSXQbraU"

    def list(self,offset=0,limit=1000,**kwargs):
        data = {"offset": offset, "limit": limit}
        print(kwargs)
        print(data)
        data.update(kwargs)
        url = "https://qyapi.weixin.qq.com/cgi-bin/externalcontact/groupchat/list"
        r = requests.post(
            url,
            params={"access_token": self.get_token(self.secret)},
            json=data
        )
        #todo  自动的加解密
        #todo  多环境的支撑
        self.format(r)
        return r.json()

    def get(self,chat_id):
        detail_url = "https://qyapi.weixin.qq.com/cgi-bin/externalcontact/groupchat/get"
        r = requests.post(
            detail_url,
            params={"access_token": self.get_token(self.secret)},
            json={"chat_id": chat_id}
        )
        self.format(r)
        assert r.json()["errmsg"] == "ok"
        assert len(r.json()["group_chat"]["member_list"]) > 0
        return r.json()
