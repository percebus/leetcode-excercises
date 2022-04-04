from typing import List

SHIP = 1
SPACE = 0


def calculate_hit_probability(rows: List[List[int]]) -> float:
    flattened = [
        column
        for row in rows
        for column in row]
    spaces = len(flattened)
    ships = flattened.count(SHIP)
    return ships / spaces



# pylint: disable=unused-argument
def getHitProbability(R: int, C: int, G: List[List[int]]) -> float:
    return calculate_hit_probability(G)
# pylint: enable=unused-argument
