def get_data(file_name):
    policy_list = []
    password_list = []
    with open(file_name) as file:
        for line in file:
            policy, password = line.strip().split(":")
            count, letter = policy.split(" ")
            count_min, count_max = count.split("-")
            password_list.append(password)
            policy_list.append([int(count_min), int(count_max), letter])
    return policy_list, password_list


if __name__ == "__main__":
    password_policy, passwords = get_data("puzzle_input2.txt")
    valid_password = 0

    for i in range(len(passwords)):
        min, max, given_letter = password_policy[i]
        if max >= passwords[i].count(given_letter) >= min:
            valid_password += 1
    print(valid_password)
