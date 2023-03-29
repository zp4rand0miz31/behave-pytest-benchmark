from pytest_eucalyptus import before, step, world  # type: ignore

# you can define steps whereever you want, the only condition is that you import pytest_eucalyptus in your module
import logging

logger = logging.getLogger("filtering")


@step(r"A stupid step")
def a_stupid_step(self):
    """A stupid step"""

    logger.info(f"running step : {self.sentence}")
