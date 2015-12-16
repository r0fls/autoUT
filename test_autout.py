import unittest
import autout

class Test_autout(unittest.TestCase):

    def test_top_level_functions(self):
        self.assertEqual(autout.top_level_functions(),)

    def test_parse_ast(self):
        self.assertEqual(autout.parse_ast(),)

    def test_autout(self):
        self.assertEqual(autout.autout(),)

if __name__ == '__main__':
    unittest.main()