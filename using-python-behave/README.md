
# Define a new test suite

- Create a new directory `{testsuite}_features`
- Create a subdirectory `steps
- Create new .feature files in it
- Create a new `conftest.py` that can define new parameters for instance
- Import the steplib from the conftest, you need to explictly import new modules.

# Define new global or specific parameters

- Create a `conftest.py` file
- Hook the function :
```python
def pytest_addoption(parser):
    """ This is a hook function. Parser is a argparse object"
```