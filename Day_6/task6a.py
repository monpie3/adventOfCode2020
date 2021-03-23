def get_data(filename):
    with open(filename) as file:
        answers = file.read().split("\n\n")
        answers = [person.split("\n") for person in answers]
    return answers


def count_yes(group):  # everyone in group
    counted_yes = {}
    common_yes = 0

    for person in group:
        for answer in person:
            counted_yes[answer] = counted_yes.get(answer, 0) + 1
            # get allows you to specify a default value if the key does not exist.

    for v in counted_yes.values():
        if len(group) == v:
            common_yes += 1

    return common_yes


if __name__ == "__main__":

    answers = get_data("puzzle_input6.txt")
    total = 0

    for group in answers:
        total += count_yes(group)

    print("Puzzle answer:", total)
