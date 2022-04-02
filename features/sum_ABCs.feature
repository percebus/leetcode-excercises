Feature: ABCs
  # SRC: https://www.facebookrecruiting.com/portal/coding_puzzles/?puzzle=513411323351554
  #
  # Constraints
  #  * 1 ≤ A,B,C ≤ 100

  Scenario Outline: Positive Numbers
    Given three integers <A>, <B>, and <C>
     When I call getSum
     Then it determines their <result>
  Examples:
  |  A  |  B  |  C  | result |
  |   1 |   2 |   3 |      6 |
  | 100 | 100 | 100 |    300 |
  |  85 |  16 |  93 |    194 |
