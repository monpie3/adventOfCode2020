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
                dic_rule[bag_name] = int(num_of_bags)
            if bag == "no other":
                dic_rule["no other"] = 1
        rules_list_of_dic.append(dic_rule)
    return rules_list_of_dic


def get_bag(your_color):
    rules = get_rules("puzzle_input7.txt")
    bags_in = {}
    for rule in rules:
        if rule["name"] == your_color:
            bags_in[your_color] = list(rule.items())[1:]  # index 0 - name)
    return bags_in


def count_children(bag_collections, top_bag_name):
    total_sum = 0
    top_level_bag = get_bag(top_bag_name)
    print(f"Currently counting bags inside {top_bag_name}.")

    top_level_bag_inside = [item for sublist in top_level_bag.values() for item in sublist]
    print("enumerate by", top_level_bag_inside)

    for (current_bag_type, current_bag_type_count) in top_level_bag_inside:
        print(f"There are {current_bag_type_count} of {current_bag_type} inside {top_bag_name}.")
        if current_bag_type == "no other":
            return total_sum
        else:
            # Add the number of bags of the current type to the count.
            total_sum += current_bag_type_count
            bags_inside_current_bag_type_count = count_children(bag_collections, current_bag_type)

            # Count the bags inside each bag of the current type, multiply it by the number of the current type,
            # then add it to the count.
            total_sum += bags_inside_current_bag_type_count * current_bag_type_count

    return total_sum


if __name__ == '__main__':
    bags = get_bag("shiny gold")
    print(bags)
    puzzle_answer = count_children(bags, "shiny gold")
    print("Puzzle answer:", puzzle_answer)
