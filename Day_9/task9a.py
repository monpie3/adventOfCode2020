def get_encrypted_data(filename):
	with open(filename) as file:
		data = file.read().splitlines()
		data = map(int, data)
	return list(data)


def get_valid_numbers(encrypted_data, preamble, step):
	pairs = set()
	for i in range(step, preamble + step):
		for j in range(step, preamble + step):
			# the two numbers in the pair must be different.
			if encrypted_data[i] != encrypted_data[j]:
				pair = encrypted_data[i] + encrypted_data[j]
				pairs.add(pair)
	return pairs


def get_num_which_dont_follow_rule(encrypted_data, preamble):
	follow_rule = True
	step = 0
	while follow_rule:
		pairs = get_valid_numbers(encrypted_data, preamble, step)
		if encrypted_data[preamble+step] not in pairs:
			return encrypted_data[preamble+step]
		step += 1  # increment after checking because preamble is len and the last element id of preamble is preamble-1


if __name__ == '__main__':
	encrypted_data = get_encrypted_data("puzzle_input.txt")
	num = get_num_which_dont_follow_rule(encrypted_data, 25)
	print("Puzzle answer:", num)
