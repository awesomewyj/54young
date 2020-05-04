def inc(x):
    return x + 1


def test_answer():
    assert inc(3) == 5


def setup_function():
    print("setup function")


class TestClass:
    def setup(self):
        print("setup")

    @classmethod
    def setup_class(cls):
        print("setup_class")

    def test_one(self):
        x = "this"
        assert "h" in x

    def test_two(self):
        x = "hello"
        assert hasattr(x, "check")
