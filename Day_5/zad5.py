def check_seat_row(boarding_pass):
    max_row = 127
    min_row = 0
    for letter in boarding_pass[:7]:
        if letter == "F":  # lower
            min_row = min_row
            max_row = max_row - int((max_row-min_row)/2)-1
        elif letter == "B":  # upper
            min_row = min_row+int((max_row-min_row)/2)+1
            max_row = max_row

    return min_row, max_row


def check_seat_column(boarding_pass):
    max_col = 7
    min_col = 0
    for letter in boarding_pass[7:]:
        if letter == "L":  # lower
            min_col = min_col
            max_col = max_col - int((max_col-min_col)/2)-1
        elif letter == "R":  # upper
            min_col = min_col+int((max_col-min_col)/2)+1
            max_col = max_col
    return min_col, max_col


if __name__ == "__main__":
    with open("puzzle_input5.txt") as file:
        boarding_passes = file.read().splitlines()

    id_list = []
    seat_list = []

    for boarding_pass in boarding_passes:
        row = check_seat_row(boarding_pass)[0]
        column = check_seat_column(boarding_pass)[0]
        seat_list.append([row, column])
        id_list.append(row*8 + column)

    print("Puzzle answer (1st):", max(id_list))

    # part 2
    for id1 in id_list:
        for id2 in id_list:
            if id1-id2 == 2 and (id1+id2)/2 not in id_list:
                # because "the seats with IDs +1 and -1 from yours will be in your list
                print(f"Puzzle answer (2nd). My seat ID is between {id1} and {id2}.")
