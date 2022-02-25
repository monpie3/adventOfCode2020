def get_adapters(filename):
	with open(filename) as file:
		data = file.read().splitlines()
		data = map(int, data)
	return set(data)   # count the joltage differences, so set is enough, same num - sum num = 0 difference


def count_joltage_differences(adapters):
	effective_rating = 0
	diff_1 = 0
	diff_3 = 0
	for i in range(len(adapters)):
		joltage_rating = range(effective_rating + 1, effective_rating + 4)
		for j in joltage_rating:
			if j in adapters and j-effective_rating == 1:
				diff_1 += 1
			if j in adapters and j-effective_rating == 3:
				diff_3 += 1
			if j in adapters:
				effective_rating = j
				break
	# your device's built-in adapter is always 3 higher than the highest adapter
	diff_3 += 1
	return diff_1, diff_3


if __name__ == '__main__':
	adapters = get_adapters("puzzle_input.txt")
	diff_1, diff_3 = count_joltage_differences(adapters)
	print(f"Puzzle answer. There are {diff_1} differences of 1 jolt and {diff_3} differences of 3 jolts. "
		  f"Number of 1-jolt differences multiplied by the number of 3-jolt differences: { diff_1 * diff_3}")
