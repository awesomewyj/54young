import pytest
from jsonpath import jsonpath

from test_requests.test_wework.api.base_api import BaseApi
from test_requests.test_wework.api.tag import Tag


class TestDDD:

    ##todo 单文件改成多文件

    data = BaseApi.yaml_load("test_tag_all.yaml")

    @classmethod
    def setup_class(cls):
        cls.tag = Tag()
        cls.reset()




    @pytest.mark.parametrize("name",data["data"][0:1])
    def test_delete(self,name):
        self.tag.params={"name" : name}
        self.tag.steps_run(self.data['steps'])


    @classmethod
    def reset(cls):
        ###删除测试数据
        ###删除测试组
        cls.tag.get()
        for name in [ "demo1", "demo2", "中文测试", "中文_1", "123", " ", "*", "👿", "", "${name}"]:
            x = cls.tag.jsonpath(f"$..tag[?(@.name=='{name}')]")
        ##搜索  查询是否有重复
            if isinstance(x, list) and len(x) > 0:
                cls.tag.delete(tag_id=[x[0]["id"]])


    def teardown(self):
        ##用例执行被强行kill时可能不会执行
        self.reset()


    def test_xxx(self):
        self.tag.xxx
