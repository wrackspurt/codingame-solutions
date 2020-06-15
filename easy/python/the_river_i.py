"""
THE RIVER I
Difficulty: Easy
Link: https://www.codingame.com/training/easy/the-river-i-
"""

r_1 = int(input())
r_2 = int(input())


def get_next(r):
    next_r = r
    while r > 0:
        next_r += r % 10
        r -= r % 10
        r /= 10
    return int(next_r)


while r_1 != r_2:
    if r_1 < r_2:
        r_1 = get_next(r_1)
    else:
        r_2 = get_next(r_2)

print(r_2)
