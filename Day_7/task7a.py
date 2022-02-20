def get_rules(filename):
    rules_list_of_dic = []
    with open(filename) as file:
        rules = file.read().splitlines()
        rules = [rule.replace(".", "") for rule in rules]
        rules = [rule.replace("bags", "") for rule in rules]
        rules = [rule.replace("bag", "") for rule in rules]
        rules = [rule.replace("contain", ",") for rule in rules]
        rules = [rule.split(",") for rule in rules]
        rules = [[el.strip() for el in rule] for rule in rules]

    for rule in rules:
        dic_rule = {}

        for i, bag in enumerate(rule):
            if i == 0:
                dic_rule["name"] = bag
            if bag != "no other" and i != 0:
                num_of_bags, bag_name = bag.split(" ", 1)
                dic_rule[bag_name] = num_of_bags
                # [int(letter) for letter in bag.split() if letter.isdigit()]
        rules_list_of_dic.append(dic_rule)
    return rules_list_of_dic


def get_number_of_valid_outermost_bag(your_color, rules):
    can_contain_num = 0
    bags_which_can_contain = set()
    for rule in rules:
        # print(rule)
        if your_color in rule.keys():  # directly
            can_contain_num += 1
            bags_which_can_contain.add(rule["name"])

    # print(keys_which_can_contain)
    sth_new = True
    while sth_new and len(bags_which_can_contain) != 0:
        it = bags_which_can_contain.copy()
        for checking_bag in it:
            for rule in rules:
                if checking_bag in rule.keys():
                    bags_which_can_contain.add(rule["name"])
                    sth_new = True

        if not(len(bags_which_can_contain) - len(it)):
            sth_new = False

    # print(keys_which_can_contain)

    for rule in rules:
        if any(non_directly in rule.keys() for non_directly in bags_which_can_contain) \
               and your_color not in rule.keys():  # non_directly
            can_contain_num += 1
            bags_which_can_contain.add(rule["name"])

    return can_contain_num, bags_which_can_contain


if __name__ == '__main__':

    regulations = get_rules("puzzle_input7.txt")
    print(*regulations[:5], end="\n")
    outermost_bag_num, outermost_bag_name = get_number_of_valid_outermost_bag("shiny gold", regulations)
    print(outermost_bag_num, outermost_bag_name)
