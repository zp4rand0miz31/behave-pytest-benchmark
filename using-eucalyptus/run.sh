#!/bin/bash

# in this run, we ALWAYS ignore the @wip tests

# This runs the broken tests
pytest -m "broken and not wip" -v
# tests the marker on features : the feature with
pytest -m "marker_on_feature and not broken and not wip" -v
# tests the marker on scenario
pytest -m "marker_on_scenario and not broken and not wip" -v
