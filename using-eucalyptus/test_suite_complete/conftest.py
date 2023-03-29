import pytest

from pytest_eucalyptus import step

# import all the steps
from test_suite_complete.filtering import a_stupid_step
import test_suite_complete.failing_test  # noqa  # the import is required by eucalyptus

from test_suite_complete import success_test, filtering, test_typing  # noqa

# from . import success_test  # only works with pytest --import-mode=importlib


@step("A basic step recycling other step")
def a_basic_step_recycling_other_steps(context):
    # call directly the other step
    a_stupid_step(context)
