import pytest
from jsonpath import jsonpath

from test_requests.test_wework.api.base_api import BaseApi
from test_requests.test_wework.api.tag import Tag


class TestTag:

    data = BaseApi.yaml_load("test_tag_data.yaml")
    steps = BaseApi.yaml_load("test_tag_step.yaml")

    @classmethod
    def setup_class(cls):
        cls.tag = Tag()
        cls.reset()


    @classmethod
    def init(cls):
        cls.data = cls.tag.yaml_load("test_tag_data.yaml")


    def test_get(self):
        r =self.tag.get()
        print(self.tag.jsonpath("$..tag[?(@.name!='')]"))
        print(self.tag.jsonpath("$..tag[?(@.name=='demo3')]"))
        # print(self.tag.jsonpath(r, "$..tag[?(@.name=='demo1')]")[0])

        assert r["errcode"] == 0


    # def test_get_api(self):
    #
    #     r= self.tag.get_api()
    #
    #     assert r["errcode"] == 0



    def test_add(self):
        r = self.tag.add("demo1")
        assert r["errcode"] == 0



    # @pytest.mark.parametrize("name", [
    #     "demo1", "demo2", "中文测试", "中文_1", "123", " ", "*", "👿", ""
    # ])
    @pytest.mark.parametrize("name",data["test_delete"])
    def test_delete(self,name):
        path = "$..tag[?(@.name!='')]"
        r = self.tag.get()
        x= self.tag.jsonpath(f"$..tag[?(@.name=='{name}')]")
        ##搜索  查询是否有重复
        if isinstance(x,list) and len(x)>0:
            self.tag.delete(tag_id=[x[0]["id"]])

        ##开始
        r = self.tag.get()
        size = len(self.tag.jsonpath(path))
        ##添加新标签
        self.tag.add(name)
        r = self.tag.get()
        assert len(self.tag.jsonpath(path)) == size+1

        ##删除新标签
        r = self.tag.get()
        tag_id = self.tag.jsonpath(f"$..tag[?(@.name=='{name}')]")[0]["id"]
        self.tag.delete(tag_id=[tag_id])
        r = self.tag.get()
        assert len(self.tag.jsonpath(path)) == size


    @pytest.mark.parametrize("name",data["test_delete"][0:1])
    def test_delete(self,name):
        self.tag.params={"name" : name}
        self.tag.steps_run(self.steps['test_delete'])


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
