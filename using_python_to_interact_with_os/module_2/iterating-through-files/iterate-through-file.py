#!/usr/bin/env/ python

# with open("spider.txt") as file:
#     for line in file:
#         print(line.upper())
# file.close()

# ====================================

with open("spider.txt") as file:
    for line in file:
        # strip() command is used to remove extra whitespace
        print(line.strip().upper())
file.close()

# ====================================

# file = open("spider.txt")
# lines = file.readlines()
# file.close()
# lines.sort()
# print(lines)