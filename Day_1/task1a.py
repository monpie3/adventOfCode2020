def get_data(file_name):
    data = []
    with open(file_name) as f:
        for line in f:
            data.append(int(line))
    return data


if __name__ == "__main__":
    puzzle_input = get_data("puzzle_input.txt")

    for i in range(len(puzzle_input)):
        for j in range(len(puzzle_input)-1, i, -1):
            if puzzle_input[i] + puzzle_input[j] == 2020:
                print("puzzle answer", puzzle_input[i] * puzzle_input[j])
                print(puzzle_input[i], puzzle_input[j])
