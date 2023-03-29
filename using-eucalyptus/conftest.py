import pytest
from pytest import fixture

import logging

print("root conftest is loading")


@pytest.fixture
def cmdopt(request):
    return request.config.getoption("--cmdopt")


def pytest_configure(config):
    logging.getLogger("root").setLevel(logging.DEBUG)


def pytest_addoption(parser):
    """Pytest hook that defines list of CLI arguments with descriptions and default values

    :param parser: pytest specific argument
    :return: void
    """
    group = parser.getgroup("toto")
    group.addoption(
        "--tags2", action="store", dest="tags_toto", default="", help="Set tags to run."
    )
    group.addoption(
        "--cmdopt",
        action="store",
        default="type1",
        help="my option: type1 or type2",
        choices=("type1", "type2"),
    )
    parser.addoption(
        "--global-option1",
        action="store",
        default="global_option1",
        help="a global option 1 defined by a developer, in order to help some configuration",
    )

    print(parser)
    print(dir(parser))
    print(parser.prog)
