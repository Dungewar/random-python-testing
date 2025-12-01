import random

FRIENDS = 8
PEOPLE = 32
GROUPS = 4
TIMES = 2

people = []
groups = []
for i in range(0, PEOPLE):
    if random.randint(0, FRIENDS) < FRIENDS:
        people.append("F")
        FRIENDS -= 1
    else:
        people.append("P")
    PEOPLE -= 1

for i in range(0, PEOPLE/GROUPS):
    groups.append([])
