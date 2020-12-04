### ADVENT OF CODE 2020

import os
import re
from functools import reduce


path = "C:\\Users\Lenovo\\Documents\\GitHub\\advent_of_code"


# DAY 3

print("Day 3")

# Part 1
# In the input file, . represents free space and # represents a tree. Assuming that the slope is three spaces to the right, then one down, how many trees are encountered?

print("part 1:")

f3 = open(os.path.join(path, "day3_input.txt"), "r")

trees = 0
line_counter = 1
index = 3

for line_raw in f3:
    line = line_raw.strip()
    line_length = len(line) - 1
    if line_counter == 1:
        line_counter += 1
    else:
        if index <= line_length:
            if line[index] == "#":
                trees += 1
                index += 3
            else:
                index += 3
        elif index > line_length:
            index = index - len(line)
            if line[index] == "#":
                trees += 1
                index += 3
            else:
                index += 3

print(trees)       


# Part 2
# Now we need to put in several different slopes (in tuple list below) and multiply the results.

print("part 2:")

def find_trees(right, down):
    f3 = open(os.path.join(path, "day3_input.txt"), "r")
    rel_line = 1 + down
    line_counter = 1
    index = right
    trees = 0
    for line_raw in f3:
        line = line_raw.strip()
        line_length = len(line) - 1
        if line_counter < rel_line:
            line_counter += 1        
        elif line_counter == rel_line:
            if index <= line_length:
                if line[index] == "#":
                    trees += 1
                    index += right
                else:
                    index += right
            elif index > line_length:
                index = index - len(line)
                if line[index] == "#":
                    trees += 1
                    index += right
                else:
                    index += right
            line_counter += 1
            rel_line += down
    return trees

slopes = [
    (1, 1),
    (3, 1),
    (5, 1),
    (7, 1),
    (1, 2)
    ]

res_list = []

for slope in slopes:
    res_list.append(find_trees(slope[0], slope[1]))

print(reduce(lambda x, y: x*y, res_list))


quit()


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
