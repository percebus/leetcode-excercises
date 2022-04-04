Feature: Director of Photography
  # SRC: https://www.facebookrecruiting.com/portal/coding_puzzles/?puzzle=870874083549040
  #
  # A photography set consists of N cells in a row, numbered from 1 to N in order,
  # and can be represented by a string C of length N.
  # Each cell i is one of the following types
  #
  # A photograph consists of
  #  * a photographer
  #  * an actor
  #  * and a backdrop
  #
  # Such that each of them is placed in a valid cell,
  # and such that the actor is between the photographer and the backdrop.
  # Such a photograph is considered artistic
  #  * if the distance between the photographer and the actor is between X and Y cells (inclusive),
  #  * and the distance between the actor and the backdrop is also between X and Y cells (inclusive).
  #
  # Determine the number of different artistic photographs
  # which could potentially be taken at the set.
  # Two photographs are considered different if they involve
  #   * a different photographer cell,
  #   * actor cell,
  #   * and/or backdrop cell.
  #
  # Constraints
  #  * 1         ≤ N ≤ 200
  #  * 1 ≤ X ≤ Y ≤ N


  Scenario Outline: Short samples
    Given a <mask> string 'C', of <length> 'N'
      And distance between <minimum> and <maximum>
     When I call getArtisticPhotographCount
     Then I get the number of different artistic <photographs> which could potentially be taken at the set
  Examples:
# |     constraint    |      distance     |             |
# |    C     |   N    |    X    |    Y    |    result   |
  |   mask   | length | minimum | maximum | photographs |
  | APABA    |   5    |       1 |       2 |           1 |
  | APABA    |   5    |       2 |       3 |           0 |
  | .PBAAP.B |   8    |       1 |       3 |           3 |
  | .PBAAP.B |   8    |       1 |       4 |           4 |
