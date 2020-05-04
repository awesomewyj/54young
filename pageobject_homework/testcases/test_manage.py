from pageobject_homework.page.manage import Manage


class TestManage:
    def setup(self):
        self.manage = Manage(reuse=True)



    def test_manage(self):
        self.manage.load_picture()
        assert "9.jpg"  in self.manage.get_picture()