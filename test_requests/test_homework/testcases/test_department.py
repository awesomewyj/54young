import requests
import pytest
from test_requests.test_homework.api.department import DepartMent
from test_requests.test_homework.api.wework import WeWork


class TestDepartMent:

    def setup(self):
        self.department = DepartMent()

    def test_token(self):
        r = WeWork.get_access_token(self.department.secret)
        print(r)
        assert   r["errmsg"]  == "ok"


    def test_creat(self):
        r = self.department.creat("test_first",1)
        assert  r["errmsg"] == "created"


    def test_update(self):
        r = self.department.creat("test_second", 2)
        new_id = r["id"]
        r = self.department.update(new_id, name="second")
        assert r["errmsg"] == "updated"

    def test_delete(self):
        r = self.department.creat("test_delete", 2)
        delete_id = r["id"]
        r = self.department.delete(delete_id)
        assert r["errmsg"] == "deleted"

    def test_get(self):
        # r = self.department.creat("test_get")
        # get_id = r["id"]
        r = self.department.get()
        print(r)
        assert r["errmsg"] == "ok"

    # def teardown(self):


    #
    # @pytest.mark.parametrize("a", [{"abc":1,"dd":2, "ff":2},{"kkk":1}])
    # def test_dict(self, a):
    #     print(a)