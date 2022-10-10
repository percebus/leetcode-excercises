Feature: All Wrong

  # SRC: https://www.facebookrecruiting.com/portal/coding_puzzles/?puzzle=1082217288848574
  #
  # There's a multiple-choice test with N questions, numbered from 1 to N.
  # Each question has 2 answer options, labelled A and B.
  # You know that the correct answer for the ith question is the ith character in the string C,
  # which is either "A" or "B", but you want to get a score of 0 on this test by answering every question incorrectly.
  # Your task is to implement the function getWrongAnswers(N, C) which returns a string with N characters,
  # the ith of which is the answer you should give for question ii in order to get it wrong (either "A" or "B").
  #
  # Constraints
  #  * 1 ≤ N ≤ 100
  #  * Ci ∈ {"A","B"}


  Scenario Outline: _
    Given a multiple-choice test with <N> questions, numbered 1 to N
      And a string with <correct> answers, each labelled A and B
     When I call getWrongAnswers(N, C)
     Then I get a string with the <wrong> answers

  # FIXME steps going to wrong step/*.py
  Examples:
# |   |     answers     |
  | N | correct | wrong |
# | 1 | A       | B     |
# | 1 | B       | A     |
# | 2 | AA      | BB    |
# | 2 | AB      | BA    |
# | 2 | BA      | AB    |
# | 2 | BB      | AA    |
# | 3 | AAA     | BBB   |
# | 3 | ABA     | BAB   |
# | 3 | AAB     | BBA   |
# | 3 | ABB     | BAA   |
# | 3 | BBB     | AAA   |
# | 3 | BAB     | ABA   |
# | 3 | BAA     | ABB   |
# | 5 | BBBBB   | AAAAA |
# | 5 | AAAAA   | BBBBB |
