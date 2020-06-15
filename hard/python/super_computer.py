"""
SUPER COMPUTER
Difficulty: Hard
Link: https://www.codingame.com/training/hard/super-computer
"""


def activity_selector(activities):
    """This algorithm is used to solve the Activity selection problem
    (the problem is to select the maximum number of activities that can be
    performed by a single person or machine, assuming that a person can only
    work on a single activity at a time). It is called Greedy Iterative Activity Selector,
    because it is first of all a greedy algorithm, and then it is iterative."""
    activities.sort(key=lambda a: a[1])  # sorting the list of activities in increasing order by ending day
    s = list()  # creating the list to store the selected activities
    s.append(activities[0])  # initializing the list with the activity that has the earliest ending day
    previous_index = 0  # creating the variable that keeps the index of previously selected activity
    for i in range(1, len(activities)):  # iterating from the 2nd element of the activity list
        previous_finish = activities[previous_index][1]  # keeping the ending day of the previous activity
        current_start = activities[i][0]  # keeping the starting day of the current activity
        if current_start > previous_finish:  # comparing the ending of previous and the starting of current activities
            s.append(activities[i])
            previous_index = i
    return len(s)  # returning the number of activities that do not clash with each other


calculations = list()  # the list where'll be the tuples with starting and ending days
n = int(input())
for i in range(n):
    j, d = [int(j) for j in input().split()]
    j_end = j + d - 1  # the ending day of calculation
    calculations.append((j, j_end))

print(activity_selector(calculations))
