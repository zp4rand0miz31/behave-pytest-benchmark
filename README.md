# python-behave vs pytest-bdd feature benchmark

As an engineering manager, I need to choose the best framework to my company in order to leverage an easy to use, easy to extend and robust framework for BDD tests.

This repository aims at sharing my discoveries while working on improving my existing test base, in the direction of using the BDD approach (Behavior Driver Development).

Many frameworks exists for several languages, but I focus on Python here.

I compare several frameworks of the python eco-system that allows BDD:

 - python-behave
 - pytest-bdd
 - pytest-eucalyptus

Disclaimer: the sole purpose of this repository is to keep track of our benchmark steps. Some points are probably not solved yet, and our analysis may be partial or wrong. We only intend to share our discoveries, that might help other to get an idea of each framework.

## What is important in a test framework ?

I use the following hypothesis, from my experience:
 - writing test is painful
 - debugging tests is always painful and lacks the right debug (log) information

Some key points for a daily usage:

1. ability to add new tests quickly
2. logging capabilities
3. test selection capabilities
4. code scalability and coherence

To create this benchmark, we developed a series of tests with both `behave` and `pytest-eucalyptus`.

# Results

## Ability to add new tests quickly

### With python-behave

- Write a new <feature name>.feature file with Given, When, Then stanza.
- run behave, a dump of unimplemented steps will be provided that can almost copy-paste with no efforts
- In case you need to reuse Steps, you can run `behave --catalog` to list them.
- To implement the steps, simply create a new python module file into the 'steps' subdirectory of your testsuite.

### With pytest-bdd

You need to create a `test_<feature>.py` to follow pytest `test_*.py` model.


## Daily usage

### Command line interface

Behave provides quite a bunch of options, the most useful are:

  - `behave --stop` :  stops on first fail (useful to dig into problems when they happens)
  - `behave --summary` : provides a text report at the end of the tests. Note pytest-bdd does this "by default", but it's more friendly with behave.



## 3. Test selection capabilities

### 3.a Tags

Both pytest-bdd and python-behave provide tags as it's part of the Gherkin language.



## 4. Code scalability and coherence



### 4.a test suites

You might want to split your tests in big categories (related or not related to features). One might think of splitting tests into performance, non-regression and user-conformance testing strategies.

Another way to

# Some general remarks when compariing

## Common remarks on python-behave vs pytest-bdd

1. Basic rendering of Gherkin steps are beautiful on behave.

Using pytest, the option --gherkin-terminal-reporter is to be used. /!\ Does not seem to work for now.

2. Pytest-bdd requires test_*.py files to declare for which scenario they are bound.

Behave is more "ready out of the box"

3. Test context in python-behave are opaque objects. With pytest-bdd, the dependency injection of the fixture system can
help add more typing. However, this is still a manual effort by the developer.

None of the frameworks are perfect on static typing requirements. Pytest-bdd allows static typing, but the
fixture declaration needs to be handled by the developer. The `target_fixture` allows dynamic override of a fixture, which
can break the typing system and mypy checks.

4. Undefined steps

By default behave provides a report and some generated code to implement missing steps. Pytest-bdd requires a manual action using `pytest-bdd generate file.feature` to generate missing steps. The missing steps shall have a @xfail declared as it's unimplemented, or maybe a @wip that should be handled by default. That would allow easy un-coupling of written Feature files that are waiting for implementation.

5. Basic tags are part of the worflow on behave

Behave provides a @wip tag that can be used on feature file at the scenario level or feature level. This is very handy. Does pytest-bdd handle this ?

6. Logging


7. Concept of testsuite

# Gherkin compliance

## Scenario Outlines

Scenario outlines are defined in Gherkin via :

```gherkin
Feature: feature X
  Scenario Outline: This is a scenario outline with variable <car_name>

    Given a driver
    When the driver drives
    """ This is multiline data
    """
    Then the car moves


  Examples:
      | car_name   | driver           |
      | xantia     | john doe         |
      | fuego      | marcelo gonzatti |

```

## Tag support



- G1: I need a framework that implements the most modern Gherkin specification, at least for :
    - examples
    - scenario outline
    - tag support (or fixtures or test filtering)
    - test pre-requisite

    - multiline data in steps definitions:
      - behave, eucalyptus: ok
      - pytest bdd: ko



- G2 I need to handle Scenario Outlines
  - "Examples tables":
    - behave, eucalyptus: ok
    - pytestbdd : ko, need some patches to get it working (succeeded in doing so)
- G3 I need to handle Examples
- G4 I need to handle regexp




## Test Case Management

### Skip / List unimplemented tests

Skipping unimplemented tests, that means, BDD tests whose steps are not found, can be very useful when your workflow allows defining tests but not implementing them at the same time

* With `behave`: a `@wip` tag is natively supported and
- I want to sort tests with tags (flaky, long, critical etc...)
  - behave:
  - gfd
  - gf
- I have test suite management on top of feature, to help group them
  - behave: there exist a test suite prefix named "stage" (`--stage`). This prefix is prepended to the "features" directory name in which features resides.
  - pytest derivates: TODO


## Conception

### Gherkin Steps Catalog

I want to list the reusable steps in order to quickly design new Gherkin files.

* With `behave`, this is builtin: `behave --steps-catalog` does this.
* With `eucalyptus`, the best we can achieve is the "test collection" via `pytest --co`, which lists all the tests and the steps inside them.
*
### Gherkin Steps Reuse

I want to design some macro-steps that does the same as a complete feature test. For instance, a ` Given {something}` inside a step might be a complete Scenario in a more detailed test done before.

This way of doing allows to do capitalize upon previous tests and have better requisites for more complex scenarios.

This also need to some dependency management between BDD tests: a failing scenario means that some other test cannot be run after.

To my knowledge, Gherkin does not allow dependency management between features and scenarios for instance.

* With `behave`, you can *TODO* (yes we can, just describe how to)

* With `eucalyptus`, you can directly a step. The only requirement is to pass the context object and import the right modules. See (eucalyptus/testsuite_complete/step_reuse.feature)[testsuite_complete]

### Gherkin File Linting / Invalid Gherkin file

Having a way to lint the Gherkin file is required to ensure the format of the Gherkin file is correct, even if some test is not implemented.

With both *behave* and *eucalyptus*, the only the only way to get a lint of the Gherkin file is to run a `pytest` collection or run `behave`, and check you don't get an error.

* With `behave`, partial or 'invalid' files (depends if we consider partial tests as invalid or not) are silently ignored.
How do we check for bad syntax ? No idea yet.

* With `eucalyptus`, the `pytest` stops when parsing the erroneous file, at collection time (for those familiar with the `test collection`). This completely stops the whole parsing of tests, this breaks early and hard, which forbid any invalid Gherkin syntax but does not allow any staging process. There's no command to allow linting either. The suggested workaround is to change the extension of the `.feature` file to `.feature.disabled` or to use the `--continue-on-collection-errors` option of `pytest`.

We did not test the exhaustive errors in the Gherkin syntax either. This test is implemented [here](./using-eucalyptus/test_suite_complete/invalid_gherkin.feature.disabled) and [here](./using-python-behave/test_suite_complete/invalid_gherkin.feature). We had to disable the file on `eucalyptus` as no syntax error is tolerated.

### Generate code for unimplemented steps

Writing a new step means that you need to write some boiler code around a `python` method, with decorators, in the right module.

Boiler plate code means:
```python

from behave import given, then, when, step  # for behave
from pytest_eucalyptus import step  # for eucalyptus

@step("A step definition")  # or use given/then/when with behave
def my_step(context):
    pass
```

 * With `behave`: when a step is not implemented, behave proposes some code to copy/paste in the module of your choice. We improved a bit the generation to get friendly function names for the proposed code. This is a nice feature of behave.
 * With `eucalyptus`: when a step is not implemented, the `pytest collection` works properly but we get a failing test. The workaround is to define a "@wip" tag and do not run these tests via `pytest -m "not wip"`.


### Dependency management / context chaining

One particular problem when coding BDD tests is that a scenario is an assembly of many steps. Each "Given" step in Gherkin is a function that provides some more context that is used later by a step.

The problem is that the chaining of steps (Given, Then, When ) leads to implicit data contract between functions that implements these steps, without any check.

Thus, a particular sequence of BDD steps can only be considered valid at test execution. This leads to less confidence when writing BDD tests.

One idea to add some robustness is to use the "dependency injection", as done by the `fixtures` from the `pytest` test framework.

Nor `behave` nor `pytest-eucalyptus` provides any solution to our knowledge.

Note: `pytest-bdd` does implement a mix of fixtures & BDD

### Code robustness / type completion in my IDE

As we want to do robust python, we want to be able to *type hint* any function parameter or return value, as any modern python3 project should do.

The main problem here is that no typed object is provided to each step.

## Test run

### Test set and test suites

I need to be able to filter a subset of tests. BDD tests can be filtered either by tags, which are part of the Gherkin specification, either by filtering the Scenario name.

One key feature here is to be able to filter on the *Outlines*, including the parameterized data. The parameterized data is the data found in the table used to derived multiple *Scenario* from a *Scenario Outline*.

- With `pytest-eucalyptus`, filtering works natively on scenario outline, without any completion. However, `pytest-eucalyptus` needs to be patched to use the data from the `Examples` tables. Test this with `pytest -k xantia -v`, that selects a scenario outline from the `parameterized_test.feature`.
* with `behave`: Same as `eucalyptus`. We did not patch `behave` yet as of now.

Tests suites can be defined easily in both framework : a simple directory is enough. `eucalyptus` requires this directory to be a module (add `__init__.py`).

### Test order management (dependency between tests)

* With *behave*: TODO

* With *eucalyptus*: the execution of the tests follows the alpha-numerical ordering, both at the testsuite level and feature (Gherkin file) level. This means that you can order your testsuite by prefixing with a sequence number the name of the testsuites and feature files. This is a bit old school but works.

To my knowledge, there's no way in Gherkin to specify the requirements of a feature or scenario test against another feature or scenario. This kind of dependency exists in the `pytest` framework. This is only helpful to reduce the execution time of a test run, when some tests fail.

### Test configuration

Passing parameter to your testsuite is really important, as you need to control the behavior of your test run.

* With *behave*: `behave -D param1=value1`. The `param1` value is then found into the `context.config.userdata` dictionary, which can be used in all the tests.
  If you want an specific configuration file to your tests, you can implement a file loading logic into the `before_all` hook that will load values from a file.

* With *pytest-bdd*: `pytest -o param1=value1` is natively supported. It overrides the `pytest.ini` file. [https://docs.pytest.org/en/7.1.x/example/simple.html#basic-patterns-and-examples](Pytest documentation) describes some way to reach. You can also add specific option via the `pytest_addoption` hook. See [using eucalyptus](/using-eucalyptus/README.md#define-new-global-or-specific-parameters)


## Test debugging

### Gherkin centric

When writing or debugging a test, it's really useful to catch the origin of the problem in a detailed way.

* With `eucalyptus`, we get information of the failing line in the Gherkin file, and the assert that fails in the python code. To reproduce: `pytest -k fails`.
* With `behave`, we get a nice report with the bdd test, the python code creating the problem and some colors. To reproduce `behave test_suite_complete/`.

Both framework show the right details. Check the "logging" section too.

Note: the fact that `pytest-bdd` is not Gherkin centric lead to its revocation from this benchmark, as we considered this a blocker point for using this other framework (which has a good maturity and lot of friendly features, by the way).

### Visualize test run errors easily

We need to easily catch the source of the error, both in Python code and Gherkin code to match what is failing and how.


- I need to catch the error easily (in python and Gherkin)
  - pytest-bdd:
  - pytest-eucalyptus: if error in Gherkin file, the line number inside the gherkin file is not reported in the pytest summary
  -  behave: not : "HOOK ERROR " when running behave. sometimes looses some print() and logging.info() ??


## Reports

### logging.info() and print() reports

We usually add some `logging` calls in the test to ensure they are debuggable in "production" (in the CI/CD jobs logs). This principle applies in the test domain, as for a real product that will be exploited in production.

Ideally, I want the following:

 - see only INFO logs (or CRITICAL) when running a test, to get a status of the running test (some steps needs to be followed)
 - be able to log DEBUG log at the same time, in a file, for debugging purposes.
 - on error, get the last DEBUG logs on the console, the exception, and the error.
 - using print() is not recommended practice as no level nor context can be attached to a log line. Moreover, mixing `logging` and `print()` can lead to interleaved lines due to internal buffering in python native libs and in logging.


 * with `behave`, by default you get a real time log in Gherkin format of the test being run.
     - live logging is enabled by default
     - current step being executed is printed in color on the console. This can be disabled.
     - during our tests, we observed that when running `behave --no-logcapture --log-level DEBUG` we lost the last log line of a sequence. The explanation comes comes from the fact that `behave` goes to start of line before printing the current step, thus erasing the current (last) log line. We should file a bugreport on `behave` project.
     - logging to a file using `behave -o <file>` is quite broken : you got the prints from behave regarding BDD steps and the `logging` API output (try `behave  test_suite_complete/ --no-logcapture --logging-level DEBUG  -o runtest.log`).
 * with `eucalyptus`:
     - to enable 'live_logging', you need to have a `pytest.ini` file with `log_cli = 1` in the root directory.
     - there's no logging of the current step being executed (and colored) as in `behave`; this is does not help getting a BDD point of view of the current execution step.
     -


### Generate a Junit report and console logging

In CI/CD, you need to get a textual INFO or DEBUG level log to quickly identify the problem. Having a Junit (or interpretable log report for CI/CD tools) report is also required, at the same time.

* with `behave`, when output to Junit is enabled, live logging does not work and logs are only produced for failing tests. This is partially explained in the command line. This can be experimented via `behave  test_suite_complete/ --no-logcapture --logging-level DEBUG  --junit  --junit-directory . -t logging` (running live log, the 'logging' tags and produce junit locally)
* with `pytest-eucalyptus`, this works pretty well : `pytest -k logging -v --log-level=DEBUG  --junit-xml=testrun.xml`.



# Summary of comparison points

Legend:
  - 'Yes' or '+' (sufficient), '++'(very nice) : requirement is ok
  - 'No' : requirement is not fulfilled
  - '~' : may need extra work to get it working
  - 'Partial' : partially fulfilled
  - 'Yes, Patched': we managed to workaround this in our code or in the framework very easily
  - 'Bug' : feature is present, but does not work well or at all
  - empty: not evaluated yet

| Requirement                         | behave                              | pytest-eucalyptus | pytest-bdd      |
| ----------------------------------- | ----------------------------------- | ----------------- | --------------- |
| Gherkin / Scenario outlines         |                                     |                   |
| Gherkin / Tag                       | Yes (+)                             | Yes (++)          |
| dependency injection                |                                     |                   |                 |
| Type completion in VSCode           |                                     |                   |                 |
| Define global parameters            |                                     |                   |                 |
| Filter by tag                       |                                     |                   |                 |
| Filter by feature/scenario name     |                                     |                   |                 |
| Filter by full outline              |                                     |                   |                 |
| skip unimplemented tests            | BUG                                 |                   |                 |
| Conception / step catalog steps     | Yes                                 | partial           |                 |
| Conception / step reuse steps       | TODO                                | Yes               |                 |
| Conception / Invalid Gherkin        | Too permissive                      | Yes very strict   |                 |
| Conception / Gherkin lint           | ~                                   | No                |                 |
| Conception / Generate code          | Yes                                 | Patching wip      |                 |
| Conception / Dependency management  | No                                  | No                | Maybe? to check |
| Conception / code robustness        | TODO                                | TODO              |                 |
| Conception / type completion in IDE | TODO                                | TODO              |                 |
| Test debugging / Gherkin centric    | Yes (++)                            | Yes (+)           | No              |
| test debugging / visualize run      | TODO                                | TODO              |                 |
| Test run / test suites              | Bug                                 | Yes               |                 |
| Test run / Test order management    | TODO                                | Yes               |                 |
| Test run / logging                  | Nice (+++), buggy in "live logging" | (++)              |                 |
| Test run / log2file + console       | file incomplete, console incomplete |                   |                 |
| Test run / log2junit + console      | Yes, live logging broken            | (+++              |                 |
| Documentation                       | yes (+++)                           |

## List of improvements we performed

We try to fix some of the problems we encountered with both `behave` and `eucalyptus`. These patches may be submitted in upstream projects, ideally.

* for `behave`:
 - some problems in the logging module are not patched, because it's quite complex. Some bugreports/PR should be submitted to the upstream project.
 -


* for `pytest-eucalyptus`:
W

### Behave

* Fix logging
* Improve template generation code
****
### Eucalyptus

* Generate boil
* Improve template generation code


## My personal feeling on all this

My *personal* conclusion below. Please note that it only engages myself, and it might not seem objective in some way.

 * `python-behave` seems more mature in terms of features. However, the project does not seem that solid in terms of features and cadence.
 * `pytest-eucalyptus` is built upon `pytest`, and profit of many features coming from it (report management for instance). The project may seem less mature on a feature point of view, but seems more easy to improve and tweak.
