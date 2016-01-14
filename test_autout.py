import unittest
import autout

class Test_autout(unittest.TestCase):

    def test_dir_iter(self):
        self.assertEqual(autout.dir_iter(),)

    def test_parse_ast(self):
        self.assertEqual(autout.parse_ast(),)

    def test_top_level(self):
        self.assertEqual(autout.top_level(),)

    def test_begin(self):
        self.assertEqual(autout.begin(),)

    def test_imports(self):
        self.assertEqual(autout.imports(),)

    def test_start(self):
        self.assertEqual(autout.start(,),)

    def test_autout_function(self):
        self.assertEqual(autout.autout_function(,,),)

    def test_initialize(self):
        self.assertEqual(autout.initialize(,,),)

    def test_autout_class(self):
        self.assertEqual(autout.autout_class(,),)

    def test_autout(self):
        self.assertEqual(autout.autout(),)

if __name__ == '__main__':
    unittest.main()