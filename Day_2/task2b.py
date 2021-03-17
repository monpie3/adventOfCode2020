def get_data(file_name):
    policy_list = []
    password_list = []
    with open("puzzle_input2.txt") as file:
        for line in file:
            policy, password = line.strip().split(":")
            count, letter = policy.split(" ")
            index_min, index_max = count.split("-")
            password_list.append(password)
            policy_list.append([int(index_min), int(index_max), letter])
    return policy_list, password_list


if __name__ == "__main__":
    valid_password = 0
    password_policy, passwords = get_data("puzzle_input2.txt")

    for i in range(len(passwords)):
        index_min, index_max, letter = password_policy[i]
        first_condition = letter == passwords[i][index_min]
        second_condition = letter == passwords[i][index_max]
        # print(index_min, index_max, letter, password_list[i], "|| letter1:", password_list[i][index_min],
        # first_condition, "letter2:", password_list[i][index_max],  second_condition)
        if first_condition ^ second_condition:
            valid_password += 1

    # despite that Toboggan Corporate Policies have no concept of "index zero"!
    # we don't have to decrease indexes because each password starts with a space

    print(valid_password)
