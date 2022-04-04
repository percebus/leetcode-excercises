Feature: Battleship

  # SRC: https://www.facebookrecruiting.com/portal/coding_puzzles/?puzzle=3641006936004915
  #
  # Constraints:
  #  * 1 ≤ R,C ≤100
  #  * 0 ≤ Gi,j ≤ 1

  # Sample test case #1
  Scenario: 3 boats in 2 x 3
    Given a battleship matrix of 2 by 3
      And with the following data:
      |  row  |
      | 0 0 1 |
      | 1 0 1 |
    When I call getHitProbability
    Then it returns a hit probability of 50%
    # 3 of the 6 cells in the grid contain battleships.
    # Therefore, the probability that your shot will hit one of them
    # is 3 / 6 = 0.5 = 50%


  # Sample test case #2
  Scenario: 4 boats in 2 x 2
    Given a battleship matrix of 2 by 2
      And with the following data:
      | row |
      | 1 1 |
      | 1 1 |
    When I call getHitProbability
    Then it returns a hit probability of 100%
    # All 4 cells contain battleships,
    # resulting in a probability of 100% of hitting a battleship.


  Scenario: 0 boats in 2 x 2
    Given a battleship matrix of 2 by 2
      And with the following data:
      | row |
      | 0 0 |
      | 0 0 |
    When I call getHitProbability
    Then it returns a hit probability of 0%
