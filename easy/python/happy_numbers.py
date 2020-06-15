"""
HAPPY NUMBERS
Difficulty: Easy
Link: https://www.codingame.com/training/easy/happy-numbers
"""


def is_happy(n):
    happies = list()
    while n != 1:
        n = sum(int(i)**2 for i in str(n))
        if n in happies:
            return False
        happies.append(n)
    return True


numbers = list()
n = int(input())
for i in range(n):
    x = input()
    numbers.append(x)
for i in numbers:
    if is_happy(i):
        print(i, ':)')
    else:
        print(i, ':(')
