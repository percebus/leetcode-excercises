Feature: Shortest Common Prefixes

  Scenario Outline: Same letter
     Given a list of <words>
      When I call longest_common_prefixes
      Then find the shortest common <prefixes> strings amongst an array of strings
  Examples:
  |       words            |     prefixes     |
  | flow, flight           | fli, flo         |
  | flight, flow           | fli, flo         |
  | flight, flower         | fli, flo         |
  | dog, dove              | dog, dov         |
  | dog, dove, duck        | dog, dov, du     |
  | dog, duck              | do, du           |
  | dove, duck             | do, du           |
# | ''                     | ''               | # FIXME


  Scenario Outline: Complex
     Given a list of <words>
      When I call longest_common_prefixes
      Then find the shortest common <prefixes> strings amongst an array of strings
  Examples:
  |                words            |       prefixes     |
  | dog, zebra, bananas             | b, d, z            |
  | dog, zebra, duck, bananas       | b, do, du, z       |
  | dog, zebra, duck, dove, bananas | b, dog, dov, du, z |



  Scenario Outline: FIXME Bugs
     Given a list of <words>
      When I call longest_common_prefixes
      Then find the shortest common <prefixes> strings amongst an array of strings
  Examples:
  |       words          |   prefixes  |     expected     |
  | flow, flower         | flowe       | flow, flowe      |
  | flight, flow, flower | fli, flowe  | fli, flow, flowe |
  | flower, flow, flight | fli, flowe  | fli, flow, flowe |
