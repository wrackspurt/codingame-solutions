"""
THE DESCENT
Difficulty: Easy
Link: https://www.codingame.com/training/easy/the-descent
"""

while True:
    h = []
    for i in range(8):
        mountain_h = int(input())
        h.append(mountain_h)
    print(str(h.index(max(h))))
