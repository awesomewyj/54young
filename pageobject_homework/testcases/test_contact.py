from pageobject_homework.page.main import Main


class Testcontact:

    def setup(self):
        self.main = Main(reuse = True)


    def test_contact(self):
        self.contact = self.main.goto_addmember().add_member()
        assert self.contact.get_memeber() == "awesome"
