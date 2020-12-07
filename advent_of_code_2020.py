### ADVENT OF CODE 2020

import os
import re
from functools import reduce
import math

path = "C:\\Users\Lenovo\\Documents\\GitHub\\advent_of_code"

# DAY 6

print("Day 6")

# Part 1
# Yes-answers per group

print("part 1:")

f6 = open(os.path.join(path, "day6_input.txt"), "r")

def yes(questions):
    q_list = []
    for letter in questions:
        q_list.append(letter)
    return len(set(q_list))

data = f6.read()
groups = re.split("\n\n", data)
yes_sum = 0

for group in groups:
    yes_sum += yes(re.sub("\n", "", group))

print(yes_sum)


# Part 2
# Questions that everyone in a group answered with "yes".

print("part 2:")

def yes_all(questions, people):
    count_list = []
    counter = 0
    for unique_l in set(questions):
        count_list.append(questions.count(unique_l))
    for c in count_list:
        if c == people:
            counter += 1
    return counter

f6 = open(os.path.join(path, "day6_input.txt"), "r")
data = f6.read()
groups = re.split("\n\n", data)

answers = 0

for group in groups:
    individ = re.split("\n", group)
    answers += yes_all("".join(individ), len(individ))

print(answers)


# DAY 5

print("Day 5")

# Part 1
# Binary boarding passes - Find the pass with the highest ID.

print("part 1:")

def BBP(boarding):
    row = range(0, 128)
    min_row = 0
    max_row = 127
    for letter in boarding[0:7]:
        if letter == "F":
            max_row = math.floor(0.5 * (max_row + min_row))
        elif letter == "B":
            min_row = math.ceil(0.5 * (max_row + min_row))
    min_seat = 0
    max_seat = 7
    for letter in boarding[7:10]:
        if letter == "L":
            max_seat = math.floor(0.5 * (max_seat + min_seat))
        elif letter == "R":
            min_seat = math.ceil(0.5 * (max_seat + min_seat))
    return min_row * 8 + min_seat

f5 = open(os.path.join(path, "day5_input.txt"), "r")

seat_list = []

for line in f5:
    seat_list.append(BBP(line.strip()))

print(max(seat_list))


# Part 2
# Find your seat!

print("part 2:")

print(sorted(set(range(seat_list[0], seat_list[-1])) - set(seat_list)))


# DAY 4

print("Day 4")

# Part 1
# Passports that contain all 8 fields should be counted as valid. If they only miss cid, they should also be included.

print("part 1:")

f4 = open(os.path.join(path, "day4_input.txt"), "r")
data = f4.read()
individuals = re.split("\n\n", data)
valid = 0

for individual in individuals:
    info = re.split("\n|\s", individual)
    if len(info) == 8:
        valid += 1
    if len(info) == 7 and re.search(r"cid", individual) == None:
        valid += 1

print(valid)

# Part 2

print("part 2:")

# Check if input in fields is valid, not just number of fields - specifically:

def check_passports(fields):
    checks = 0
    for field in fields:
        fi = field.split(":")
        if fi[0] == "byr":
            if int(fi[1]) >= 1920 and int(fi[1]) <= 2002:
                checks += 1
        if fi[0] == "iyr":
            if int(fi[1]) >= 2010 and int(fi[1]) <= 2020:
                checks += 1
        if fi[0] == "eyr":
            if int(fi[1]) >= 2020 and int(fi[1]) <= 2030:
                checks += 1
        if fi[0] == "hgt" and fi[1].endswith('cm'):
            if int(fi[1].strip('cm')) >= 150 and int(fi[1].strip('cm')) <= 193:
                checks += 1
        if fi[0] == "hgt" and fi[1].endswith('in'):
            if int(fi[1].strip('in')) >= 59 and int(fi[1].strip('in')) <= 76:
                checks += 1
        if fi[0] == "hcl":
            if re.match(r"#[a-f0-9]{6}\b", fi[1]):
                checks += 1
        if fi[0] == "ecl":
            if fi[1] in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
                checks += 1
        if fi[0] == "pid":
            if re.match(r"\d{9}\b", fi[1]):
                checks += 1
    return checks

f4 = open(os.path.join(path, "day4_input.txt"), "r")
data = f4.read()
individuals = re.split("\n\n", data)
valid = 0

for individual in individuals:
    info = re.split("\n|\s", individual)
    if len(info) == 8 and check_passports(info) == 7:
        valid += 1
    if len(info) == 7 and re.search(r"cid", individual) == None and check_passports(info) == 7:
        valid += 1

print(valid)


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
res_ls = []

for line in f:
    ls_1.append(int(line.strip()))
    ls_2.append(int(line.strip()))
    ls_3.append(int(line.strip()))
    res_ls.append(int(line.strip()))

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

