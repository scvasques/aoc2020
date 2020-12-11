import re

requiredFields = ["byr","iyr","eyr","hgt","hcl","ecl","pid"]

def passportInfoToMap(passportInfo):
    map = {}
    for i in passportInfo.split(" "):
        pair = i.split(":")
        map[pair[0]] = pair[1]
    return map

def isValid(map):
    return all(i in map for i in requiredFields)

with open("input.txt", "r") as f:
	lines = f.readlines()
lines.append("\n")
passportInfo = ""
passportInfoList = []
valid = 0
for i in lines:
    if i == "\n":
        passport = passportInfoToMap(passportInfo.replace("\n", " ").strip())
        passportInfo = ""
        if isValid(passport):
            valid += 1
    else:
        passportInfo += i
print("Number of valid passports: " + str(valid))