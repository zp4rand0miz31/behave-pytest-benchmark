#!/usr/bin/env python
# # -*- coding: UTF-8 -*-
"""

"""

from typing import Any, Dict, List
from behave import fixture, use_fixture, configuration
from behave.fixture import use_fixture_by_tag, fixture_call_params
import logging
import importlib


# from rich.logging import RichHandler
# from behave.tag_matcher import ActiveTagMatcher, setup_active_tag_values
# from behave import python_feature
# from behave.tag_matcher import ActiveTagMatcher, print_active_tags

# from dotenv import dotenv_values


# def load_dot_env_stuff(context):
#     """Loads the .env dotenv file in order to provide values into the test context.

#     Warning ! Keys are lowered() !
#     Example:

#         $ cat .env:

#     """
#     logging.debug("Loading values...")
#     values = dotenv_values()
#     for k, v in values.items():
#         _k = k.lower()
#         _v = v.lower()
#         if _k in context.config.userdata:
#             logging.warn(
#                 f"Ignoring value {_v} for key '{_k}', existing value : '{context.config.userdata[_k]}'"
#             )
#         else:

#             logging.info(f"Loading values from dotenv:   {_k} = '{_v}' ")
#             context.config.userdata[_k] = _v


def before_all(context):
    print('[test] if this is printed, print() will be displayed"')
    context.config.setup_logging()
    logging.basicConfig(
        format="%(asctime)s %(levelname)s %(message)s", datefmt="%H:%M:%S"
    )
    # logging.getLogger().addHandler(
    #     RichHandler(omit_repeated_times=False, rich_tracebacks=True, show_path=False)
    # )
    logging.info("[test] if this is printed, logging.info() will be displayed")
    # load_dot_env_stuff(context)


def before_feature(context, feature):
    # model.init(environment='test')  # what is this ?
    pass
    print(f"THIS IS THE FEATURE {feature}")


def before_scenario(context, scenario):
    # model.init(environment='test')  # what is this ?
    # pass
    # print(f"THIS IS THE SCENARIO {scenario}")
    # print(dir(scenario))
    # for i in scenario.steps:
    #     print(i)
    #     print(dir(i))
    # print(context.active_outline)
    # print(dir(context))
    # print(context.table)
    # print(context.text)
    # print(dir(context.active_outline))
    # scenario.skip()

    # the code below applies in scenario_outlines. if a table with "skip_condition" is set, it will
    # be used to skip this test based on data.
    column_that_hold_condition = None
    column_index = 0
    for header in context.active_outline.headings:
        # print(header)
        if header == "skip_condition":
            column_that_hold_condition = column_index
            break
        column_index += 1

    logging.debug(f"Found column that has skip_condition: {column_that_hold_condition}")

    if column_that_hold_condition:
        condition = context.active_outline[column_that_hold_condition]
        if condition.strip() != "":
            logging.debug(f"Evaluating condition : {condition}")
            evaluated = eval(
                condition,
                {
                    "context": context,
                    "scenario": scenario,
                    "config": context.config.userdata,
                },
            )
            print(context.vm)
            logging.debug(f"Evaluated : {evaluated}")
            if evaluated:
                logging.debug(f"Will skip this scenario because: '{condition}' is True")
                scenario.skip()

    logging.debug("")


def parse_tag_name(complete_tag: str) -> tuple[str, Dict[Any, Any]]:
    # TODO unittest
    if "(" in complete_tag and ")" in complete_tag:
        tag_name = complete_tag[0 : complete_tag.find("(")]
        param_list = complete_tag[complete_tag.find("(") + 1 : -1]
        args = dict(
            map(
                lambda x: [x[0].strip(), x[1].strip()],
                [e.split("=") for e in param_list.split(",")],
            )
        )
        return (tag_name, args)
    else:
        return (complete_tag, dict())


def before_tag(context, tag):
    if tag.startswith("fixture."):
        # TODO error handling and high quality code
        # TODO unittest on this

        stripped_tag = tag.split(".")
        logging.debug(tag)
        logging.debug(stripped_tag)

        assert len(stripped_tag) == 3
        mod_name = stripped_tag[1]
        fixture_func_name = ".".join(stripped_tag[2:])
        (n, _args) = parse_tag_name(fixture_func_name)
        logging.debug(f"Found parameter from tag: {_args}")
        mod = importlib.import_module(f"taratatest.fixtures.{mod_name}")
        logging.debug(f"Found fixture module : {mod}")
        fixture_func = mod.__getattribute__(n)
        logging.debug(f"Found fixture function: {n}")
        return use_fixture(fixture_func, context, **_args)
