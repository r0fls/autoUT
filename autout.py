import ast
import sys
from itertools import chain

def parse_ast(filename):
    with open(filename, "rt") as file:
        return ast.parse(file.read(), filename=filename)

def top_level(body):
    return (f for f in body if isinstance(f, ast.FunctionDef) or isinstance(f, ast.ClassDef))

def begin(filename):
    return imports(filename)+start(filename)

def imports(filename): 
    return 'import unittest\nimport {0}\n\n'.format(filename)

def start(name,cls=False):
    if not cls:
        return 'class Test_{0}(unittest.TestCase):\n\n'.format(name)
    else:
        return 'class Test_{0}_{1}(unittest.TestCase):\n\n'.format(name,cls)
 
def autout_function(func, filename, cls= False):
    if not cls:
        return '    def test_{1}(self):\n        '\
                    'self.assertEqual({0}.{1}({2}),)\n\n'.format(filename, func.name, ','.join('' for i in range(len(func.args.args))))
    else:
        return '    def test_{1}(self):\n        '\
                    'self.assertEqual({0}.{1}({2}),)\n\n'.format(filename, func.name, ','.join('' for i in range(len(func.args.args)-1)))

def initialize(item, filename, cls):
    if item.name == '__init__':
        return '    instance = {0}.{1}()\n\n'.format(filename, cls.name)
    else:
        return autout_function(item, 'instance', cls)


def autout_class(cls, filename):
    return chain(start(filename, cls.name),(initialize(item, filename, cls) for item in cls.body if isinstance(item, ast.FunctionDef)))
 
def autout(filename):
    tree = parse_ast(filename)
    filename = filename.replace('.py', '')
    f = open('test_{}.py'.format(filename), 'w')
    f.write(begin(filename))
    for item in top_level(tree.body):
        if isinstance(item, ast.ClassDef):
            for stmt in autout_class(item,filename):
                f.write(stmt)
        else:
            f.write(autout_function(item,filename))
    f.write("if __name__ == '__main__':\n    unittest.main()")


if __name__ == "__main__":
    for filename in sys.argv[1:]:
        autout(filename)
