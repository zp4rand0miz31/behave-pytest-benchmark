Eucalyptus
=============

# How to add a feature

- create a .feature file
- create a new python module (if necessary)
- define all the new steps into this python module
- then import this module in the conftest.py

Exploration notes
################

- does not have a way to make a dry-run : run the tests, even non unimplemented ones.




Bug found :
- if not "And ..." is defined in the steps, this will error with :

args = (<Step: "And I have a software installer">,), kwargs = {}

    @wraps(function)
    def wrapped(*args, **kwargs):
        """Run all the hooks in proper relations to the event."""
        for before_hook in before_hooks:
            before_hook(*hook_args, **hook_kwargs)

        try:
            with multi_hook(*hook_args, **hook_kwargs):
>               return function(*args, **kwargs)
E               TypeError: _() takes 0 positional arguments but 1 was given

../../pytest-eucalyptus/aloe/registry.py:130: TypeError


# Define a new test suite

- Create a new directory
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

Then, TODO, you need to get this option in your tests