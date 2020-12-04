### ADVENT OF CODE 2020

import os
import re

path = "C:\\Users\Lenovo\\Documents\\GitHub\\advent_of_code"


# DAY 2

print("Day 2")

# Part 1
# The input contains the following information: min-max letter: password
# Check whether each password contains the correct amount of letters. Count the ones that do.

print("part 1:")

f = open(os.path.join(path, "day2_input.txt"), "r")

counter = 0

for line in f:
    ls = re.split('-| |: ', line)
    min_letter = int(ls[0])
    max_letter = int(ls[1])
    letter = ls[2]
    password = ls[3].strip()
    if password.count(letter) >= min_letter and password.count(letter) <= max_letter:
        counter += 1

print(counter)


# Part 2
# The input contains the following information: position of first character-position of second character character: password
# Check whether each password contains the correct character in EXACTLY ONE of the two positions. Count the ones that do.

print("part 2:")

f = open(os.path.join(path, "day2_input.txt"), "r")

counter = 0

for line in f:
    ls = re.split('-| |: ', line)
    pos1 = int(ls[0]) - 1
    pos2 = int(ls[1]) - 1
    letter = ls[2]
    password = ls[3].strip()
    if password[pos1] == letter or password[pos2] == letter:
        if password[pos1] == password[pos2]:
            pass
        else:
            counter += 1

print(counter)


# DAY 1
# In the input file, find the two numbers that add up to 2020, then multiply them with each other.

print("Day 1")

f = open(os.path.join(path, "day1_input.txt"), "r")

ls_1 = []
ls_2 = []
ls_3 = []

for line in f:
    ls_1.append(int(line.strip()))
    ls_2.append(int(line.strip()))
    ls_3.append(int(line.strip()))

# part 1
print("part 1:")
for x in ls_1:
    for y in ls_2:
        if x + y == 2020:
            print(x * y)

# part 2
print("part 2:")
for x in ls_1:
    for y in ls_2:
        for z in ls_3:
            if x + y + z == 2020:
                print(x * y * z)
