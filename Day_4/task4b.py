import re


def get_data(filename):
    list_of_dict_passports = []

    with open(filename) as file:
        passports_list = file.read().split("\n\n")

    passports_list = [passport.replace("\n", " ") for passport in passports_list]
    passports_split = [passport.split(" ") for passport in passports_list]

    for passport_split in passports_split:
        passport_dict = {}
        for feature in passport_split:
            key, value = feature.split(":")
            passport_dict[key] = value
        list_of_dict_passports.append(passport_dict)

    return list_of_dict_passports


if __name__ == "__main__":
    passports = get_data("puzzle_input4.txt")
    required = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}
    valid_year_byr = re.compile(r'(19[2-9][0-9]|20[0][0-2])')
    valid_year_iyr = re.compile(r'(20[1][0-9]|2020)')
    valid_year_eyr = re.compile(r'(20[2][0-9]|2030)')
    valid_hgt_cm = re.compile(r'(1[5-8][0-9]|19[0-3])')
    valid_hgt_in = re.compile(r'(59|6[0-9]|7[0-6])')
    valid_hcl = re.compile(r'(#[a-f0-9]{6})')
    valid_ecl = re.compile(r'(amb|blu|brn|gry|grn|hzl|oth)')
    valid_pid = re.compile(r'([0-9]{9})')
    # or -> valid_year =  r'({})'.format('|'.join([str(x) for x in range(1920, 2003)]))

    valid_passports = 0
    for passport in passports:
        # print(required-set(passport.keys()))
        if not required-set(passport.keys()):
            valid_hgt = False
            cm_in = re.search(r"cm|in", passport["hgt"])

            if cm_in:
                if cm_in.group(0) == "cm":
                    valid_hgt = valid_hgt_cm.search(passport["hgt"])
                elif cm_in.group(0) == "in":
                    valid_hgt = valid_hgt_in.search(passport["hgt"])

            if valid_year_byr.search(passport["byr"]) and \
               valid_year_iyr.search(passport["iyr"]) and \
               valid_year_eyr.search(passport["eyr"]) and \
               valid_hcl.search(passport["hcl"]) and \
               valid_ecl.search(passport["ecl"]) and \
               valid_pid.search(passport["pid"]) and len(passport["pid"]) == 9 and \
               valid_hgt:

                valid_passports += 1

    print("Puzzle answer:", valid_passports)
