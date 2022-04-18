Feature: Sum Even Fibonacci Numbers

  # SRC: https://projecteuler.net/problem=2
  #
  # Each new term in the Fibonacci sequence is generated by adding the previous two terms.
  # By starting with 1 and 2, the first 10 terms will be:
  # 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
  #
  # By considering the terms in the Fibonacci sequence whose values do not exceed four million,
  # find the sum of the even-valued terms.

  Scenario Outline: _
    Given A <limit> number
     When I call sum_evens
     Then I get the <total> sum of all even numbers inside the Fibonacci series, up until that limit

  Examples:
  |  limit  |  total  |                          explanation                            |
  |       1 |       0 |                                                                 |
  |       2 |       2 | 2                                                               |
  |       3 |       2 | 2                                                               |
  |       4 |       2 | 2                                                               |
  |       5 |       2 | 2                                                               |
  |       6 |       2 | 2                                                               |
  |       7 |       2 | 2                                                               |
  |       8 |      10 | 2 +8                                                            |
  |       9 |      10 | 2 +8                                                            |
  |      10 |      10 | 2 +8                                                            |
  |      34 |      44 | 2 +8 +34                                                        |
  |     100 |      44 | 2 +8 +34                                                        |
  |     144 |     188 | 2 +8 +34 +144                                                   |
  |     200 |     188 | 2 +8 +34 +144                                                   |
  |     610 |     798 | 2 +8 +34 +144 +610                                              |
  |     700 |     798 | 2 +8 +34 +144 +610                                              |
  |    1000 |     798 | 2 +8 +34 +144 +610                                              |
  |    2584 |    3382 | 2 +8 +34 +144 +610 +2584                                        |
  |    3000 |    3382 | 2 +8 +34 +144 +610 +2584                                        |
  |   10000 |    3382 | 2 +8 +34 +144 +610 +2584                                        |
  |   10946 |   14328 | 2 +8 +34 +144 +610 +2584 +10946                                 |
  |   11000 |   14328 | 2 +8 +34 +144 +610 +2584 +10946                                 |
  |   20000 |   14328 | 2 +8 +34 +144 +610 +2584 +10946                                 |
  |   46368 |   60696 | 2 +8 +34 +144 +610 +2584 +10946 +46368                          |
  |   50000 |   60696 | 2 +8 +34 +144 +610 +2584 +10946 +46368                          |
  |  100000 |   60696 | 2 +8 +34 +144 +610 +2584 +10946 +46368                          |
  | 1000000 | 1089154 | 2 +8 +34 +144 +610 +2584 +10946 +46368 +196418 +832040          |
  | 4000000 | 4613732 | 2 +8 +34 +144 +610 +2584 +10946 +46368 +196418 +832040 +3524578 |