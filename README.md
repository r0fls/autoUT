# autoUT
Generate basic unit tests from working python code.

What is this good for? Not TDD.

Currently this creates a unit test file, given a python file, with skeleton tests. That is, they need the arguments and expected values filled in. So, running `python autounit.py neatProgram.py` will generate tests for the python file `neatProgram.py`.

TO DO:
- get argument types for each function
- initialize classes
