import unittest
from main import add, divide

class TestMain(unittest.TestCase):

    def test_add1(self):
        self.assertEqual(add(3, 5), 8)

    def test_add2(self):
        self.assertEqual(add(-1, 1), 0)
        
    def test_add3(self):
        self.assertEqual(add(0, 0), 0)
        
    def test_add4(self):
        self.assertEqual(add(10, -5), 5)

    def test_add5(self):
        self.assertEqual(add(2.5, 3.5), 6)

    def test_divide1(self):
        self.assertEqual(divide(10, 2), 5)

    def test_divide2(self):
        self.assertEqual(divide(-10, 2), -5)
        
if __name__ == '__main__':
    unittest.main()
