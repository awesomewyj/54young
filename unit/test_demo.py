import unittest


class TestDemo(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        print("setupcalss")

    def setUp(cls) -> None:
        print("setup")

    @classmethod
    def tearDownClass(cls) -> None:
        print("tearDownClass")

    def tearDown(cls) -> None:
        print("tearDown")

    def test_sum(self):
        x = 1 + 2
        print(x)
        self.assertEqual(4, x, f"{x} expection=3")

    def test_demo(self):
        self.assertTrue(False)


if __name__ == '__main__':
    unittest.main()
