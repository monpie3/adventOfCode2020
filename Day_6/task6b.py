def get_data(filename):
    with open(filename) as file:
        answers = file.read().split("\n\n")
        answers = [person.split("\n") for person in answers]
    return answers


def count_yes(group):  # anyone in group
    # Duplicate answers to the same question don't count extra; each question counts at most once.
    counted_yes = set()
    for person in group:
        for answer in person:
            counted_yes.add(answer)
    return len(counted_yes)


if __name__ == "__main__":
    answers = get_data("puzzle_input6.txt")
    total = 0
    for group in answers:
        total += count_yes(group)

    print("Puzzle answer:", total)
