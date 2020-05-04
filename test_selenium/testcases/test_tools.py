from test_selenium.page.main import Main
from test_selenium.page.tools import Tools


class Testtools:

    def setup(self):
        self.main = Main(reuse=True)
        self.tools = Tools(reuse=True)
        self.main.goto_tools()


    def test_picture(self):

        self.tools.goto_material_library()


