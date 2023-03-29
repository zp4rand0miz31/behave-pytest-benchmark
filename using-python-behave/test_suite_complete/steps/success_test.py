#!/usr/bin/env python

# from pytest_eucalyptus import step
from behave import step

import logging


@step("A step that succeeds")
def a_test_that_succeeds(context):
    logging.debug("DEBUG: This test will not fail for reason X, but suceed")
    logging.info("INFO: This test will not fail for reason X, but suceed")
    logging.warning("INFO: This test will not fail for reason X, but suceed")
    print("a_test_that_succeeds: This is a raw print in the code when test is ok")
    assert True  # this test assert True, and is ok.
