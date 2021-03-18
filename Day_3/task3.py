import math


def get_data(filename):
    with open(filename) as file:
        data = file.read().splitlines()
    return data


def get_num_encountered_trees(right, down, pattern):
    # prepare a slope of the right size
    times_down = len(pattern)
    len_patterns_line = len(pattern[0])
    repeat = math.ceil(times_down*right/len_patterns_line)
    slope = []
    for line in pattern:
        slope_row = []
        for _ in range(repeat):
            slope_row.extend(line)
        slope.append(slope_row)

    # sledding
    right_temp = right
    num_of_encountered_trees = 0

    for down in range(down, times_down, down):
        if slope[down][right_temp] == ".":
            slope[down][right_temp] = "0"
        else:
            slope[down][right_temp] = "X"
            num_of_encountered_trees += 1
        right_temp += right

    return num_of_encountered_trees


if __name__ == "__main__":
    pattern = get_data("puzzle_input3.txt")

    encountered_trees = [
        get_num_encountered_trees(1, 1, pattern),
        get_num_encountered_trees(3, 1, pattern),
        get_num_encountered_trees(5, 1, pattern),
        get_num_encountered_trees(7, 1, pattern),
        get_num_encountered_trees(1, 2, pattern),
    ]

    puzzle_answer = 1
    for each_slope in encountered_trees:
        puzzle_answer *= each_slope
    print(puzzle_answer)
