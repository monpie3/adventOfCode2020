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
    valid_passports = 0
    for passport in passports:
        # print(required - set(passport.keys()))
        if not required - set(passport.keys()):
            valid_passports += 1

    print("Puzzle answer:", valid_passports)
