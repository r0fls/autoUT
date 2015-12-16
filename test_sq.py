import unittest
import sq

class Test_sq(unittest.TestCase):

    def test_square(self):
        self.assertEqual(sq.square(4),16)

    def test_cube(self):
        self.assertEqual(sq.cube(2),8)

    def test_dog(self):
        self.assertEqual(sq.dog(),'woof')

if __name__ == '__main__':
    unittest.main()
