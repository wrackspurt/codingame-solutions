"""
POWER OF THOR - EPISODE 1
Difficulty: Easy
Link: https://www.codingame.com/training/easy/power-of-thor-episode-1
"""

import sys

light_x, light_y, initial_tx, initial_ty = [int(i) for i in input().split()]

while True:
    remaining_turns = int(input())
    dir_x = ""
    dir_y = ""

    print(str(initial_tx - light_x), str(initial_tx - light_y), file=sys.stderr)

    if light_x > initial_tx and initial_tx < 39:
        dir_x = "E"
        initial_tx += 1
    elif light_x < initial_tx and initial_tx > 0:
        dir_x = "W"
        initial_tx += 1

    if light_y > initial_ty and initial_ty < 17:
        dir_y = "S"
        initial_ty += 1
    elif light_y < initial_ty and initial_ty > 0:
        dir_y = "N"
        initial_ty += 1

    print(dir_y + dir_x)
