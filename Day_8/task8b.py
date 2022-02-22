import copy


def get_instructions(filename):
    with open(filename) as file:
        instructions = file.read().splitlines()
        instructions = [instruction.split() for instruction in instructions]
    return instructions


def accumulator(instructions):
    print("accumulator", instructions)
    stay_in_infinite_loop = True
    list_of_ind = []
    ind = 0
    acc = 0

    while stay_in_infinite_loop:
        if len(instructions) - 1 < ind:
            return True, acc

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
            stay_in_infinite_loop = False
            return False, "program didn't terminated"

        list_of_ind.append(ind)


def swap_op(instructions, step):
    """swaps op from nop to jmp or jmp to nop"""
    instr = copy.deepcopy(instructions)
    ops, _ = zip(*instr)
    for i in range(step, len(ops)):
        if ops[i] == "jmp":
            instr[i][0] = "nop"
            return instr, i + 1
        if ops[i] == "nop":
            instr[i][0] = "jmp"
            return instr, i + 1


def terminate_program_by_swap(instructions):
    terminated = False
    step = 0
    while not terminated:
        n_instructions, step = swap_op(instructions, step)
        terminated, acc = accumulator(n_instructions)
        print("acc", acc)
    return acc


if __name__ == "__main__":
    instructions = get_instructions("puzzle_input.txt")
    acc = terminate_program_by_swap(instructions)
    print("Puzzle answer:", acc)
