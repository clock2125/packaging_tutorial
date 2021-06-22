import unittest
from src.example_package import example


class MyTestCase(unittest.TestCase):
    def test_add_one(self):
        self.assertEqual(example.add_one(3), 4)
        self.assertEqual(example.add_one(100), 101)


if __name__ == '__main__':
    unittest.main()
