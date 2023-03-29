#!/usr/bin/env python

from pytest_eucalyptus import step

import logging


@step("A step that does x")
def a_test_that_does_x(context):
    logging.info("INFO: does X")
    assert True  # this test assert True, and is ok.
    context.value_x = "value_x"


@step("A step that does y")
def a_test_that_does_y(context):
    logging.info("INFO: does X")
    assert True  # this test assert True, and is ok.
    assert context.value_x == "value_x"

    context.value_y = "value_y"


@step("A step that does z")
def a_test_that_does_z(context):
    logging.info("INFO: does X")
    assert True  # this test assert True, and is ok.
    context.value = "value"
