import re

requiredFields = ["byr","iyr","eyr","hgt","hcl","ecl","pid"]

def passportInfoToMap(passportInfo):
    map = {}
    for i in passportInfo.split(" "):
        pair = i.split(":")
        map[pair[0]] = pair[1]
    return map

def isValid(map):
    if not all(i in map.keys() for i in requiredFields):
        return False
    if not re.search("^\d{4}$", map["byr"]) or int(map["byr"]) < 1920 or int(map["byr"]) > 2002:
        return False
    if not re.search("^\d{4}$", map["iyr"]) or int(map["iyr"]) < 2010 or int(map["iyr"]) > 2020:
        return False
    if not re.search("^\d{4}$", map["eyr"]) or int(map["eyr"]) < 2020 or int(map["eyr"]) > 2030:
        return False
    if len(map["hgt"]) < 3 or not map["hgt"][0:-2].isnumeric():
        return False
    else:
        if map["hgt"][-2:] not in ["cm", "in"]:
            return False
        elif map["hgt"][-2:] == "cm" and (int(map["hgt"][0:-2]) < 150 or int(map["hgt"][0:-2]) > 193):
            return False
        elif map["hgt"][-2:] == "in" and (int(map["hgt"][0:-2]) < 59 or int(map["hgt"][0:-2]) > 76):
            return False
    if not re.search("^#(?:[0-9a-fA-F]{3}){1,2}$", map["hcl"]):
        return False
    if map["ecl"] not in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
        return False
    if not re.search("^\d{9}$", map["pid"]):
        return False
    return True    

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