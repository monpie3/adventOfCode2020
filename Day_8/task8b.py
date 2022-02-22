def get_instructions(filename):
    with open(filename) as file:
        instructions = file.read().splitlines()
        instructions = [tuple(instruction.split()) for instruction in instructions]
    return instructions

if __name__ == "__main__":
    instructions = get_instructions("puzzle_input.txt")
    print(instructions)

    diffrent_ind = True
    list_of_ind = []
    ind = 0
    acc = 0
    while diffrent_ind:
        op, argument = instructions[ind]
        argument = int(argument)
        print("Operation:", op, argument, ". Acc before:", acc, ". i before:", ind)

        if op == "nop":
            ind += 1

        if op == "acc":
            ind += 1
            acc += argument

        if op == "jmp":
            ind += argument

        print("Operation:", op, argument, ". Acc after:", acc, ". i after:", ind)

        if ind in list_of_ind:
            print("Program would run an instruction a second time")
            diffrent_ind = False

        list_of_ind.append(ind)

    print("acc", acc)
