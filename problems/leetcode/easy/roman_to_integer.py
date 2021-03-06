

# SRC: https://leetcode.com/problems/roman-to-integer/
def roman_to_int(string):
    symbols = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    values = [
        symbols[char]
        for char in list(string)
    ]

    length = len(values)
    for idx, value in enumerate(values):
        if idx + 1 >= length:
            continue

        if values[idx] < values[idx + 1]:
            values[idx] = value * -1

#   print(values) # DEBUG only
    return sum(values)


def run(string, expected=None):
    result = roman_to_int(string)
    assert result == expected
    print('✅', end='')


def run_all():
    # Example1:
    #  * Input: s = "III"
    #  * Output: 3
    #  * Explanation: III = 3.
    run('III', expected=3)

    # Example 2:
    #  * Input: s = "LVIII"
    #  * Output: 58
    #  * Explanation: L = 50, V = 5, III = 3.
    run('LVIII', expected=58)

    # Example 3:
    #  * Input: s = "MCMXCIV"
    #  * Output: 1994
    #  * Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
    run('MCMXCIV', expected=1994)

    print('\n')


if __name__ == '__main__':
    run_all()
