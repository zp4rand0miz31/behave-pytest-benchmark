@marker_on_feature
Feature: Framework allows filtering by tag

    Developer sometimes needs to filter by tags

    Scenario: Scenario without mark, I invoke a stupid step to check if this scenario is run
        Given A stupid step

    @marker_on_scenario
    Scenario: Using marker_on_scenario, I invoke a stupid step to check if this scenario is run
        Given A stupid step

