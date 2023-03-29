#!/usr/bin/env python

# from pytest_eucalyptus import step
from behave import step
import logging


@step("A step that fails")
def a_failing_step(context):
    logging.debug("DEBUG: This test will fail for reason X")
    logging.info("INFO: This test will fail for reason X")
    logging.warning("WARNING: This test will fail for reason X")

    print("a_failing_step: This is a raw print in the code.")
    # assert False  # this test fails.
    import time

    time.sleep(1)
    print("lg")
    logging.info("INFO: This test will fail for reason Y")
    time.sleep(1)
    assert False
