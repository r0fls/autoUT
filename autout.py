import ast
import sys


def top_level_functions(body):
    return (f for f in body if isinstance(f, ast.FunctionDef))


def parse_ast(filename):
    with open(filename, "rt") as file:
        return ast.parse(file.read(), filename=filename)

def autout(filename):
    tree = parse_ast(filename)
    filename = filename.replace('.py', '')
    f = open('test_{}.py'.format(filename), 'w')
    f.write(
        'import unittest\nimport {0}\n\nclass Test_{0}(unittest.TestCase):\n\n'.format(filename))
    for func in top_level_functions(tree.body):
        f.write(
            "    def test_{1}(self):\n        self.assertEqual({0}.{1}(),)\n\n".format(
                filename, func.name))
    f.write("if __name__ == '__main__':\n    unittest.main()")

if __name__ == "__main__":
    for filename in sys.argv[1:]:
        autout(filename)
        
