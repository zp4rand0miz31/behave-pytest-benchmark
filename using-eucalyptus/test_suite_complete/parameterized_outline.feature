
Feature: Gherkin / Parameterized scenario outline
  As a BDD tester, I want to be able to define a scenario outline and select a test from

  Scenario Outline: A scenario outline that does nothing but consumes variables  <var1> to <var2>

    Given a step that does x
    Given A stupid step

    Examples: Data to consume
      | var1   | var2             |
      | xantia | john doe         |
      | fuego  | marcelo gonzatti |

  Scenario Outline: This is a scenario outline with variable <car_name>

    Given a driver
    When the driver drives
      """ This is multiline data
      """
    Then the car moves


    Examples:
      | car_name | driver           |
      | xantia   | john doe         |
      | fuego    | marcelo gonzatti |
