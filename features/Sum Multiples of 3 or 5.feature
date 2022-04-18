Feature: Sum of Multiples

  # If we list all the natural numbers below 10 that are multiples of 3 or 5,
  # we get 3, 5, 6 and 9.
  # The sum of these multiples is 23.
  Scenario Outline: 10
    Given a <limit> number
      And a few <multiples> to divide by
     When I call sum_multiples
     Then I get the expected <result>

  Examples:
    | limit | multiples | result | explanation |
    |    10 |   3       |     18 | 3    +6 +9  |
    |    10 |   3, 5    |     23 | 3 +5 +6 +9  |
    |    10 |      5    |      5 |    5        |


  # Find the sum of all the multiples of 3 or 5 below 1000.
  Scenario Outline: 1000
    Given a <limit> number
      And a few <multiples> to divide by
     When I call sum_multiples
     Then I get the expected <result>

  Examples:
    | limit | multiples | result |
    |  1000 |   3       | 166833 |
    |  1000 |   3, 5    | 233168 |
    |  1000 |      5    |  99500 |
