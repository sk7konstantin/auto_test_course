import unittest

class TestABS(unittest.TestCase):

    def test_abs1(self):
        self.assertEqual(abs(-42),42, 'Should be absolute value of a number1')

    def test_abs2(self):
        self.assertEqual(abs(-42),-42, 'Should be absolute value of a number2')

if __name__ == '__main__':
    unittest.main()
