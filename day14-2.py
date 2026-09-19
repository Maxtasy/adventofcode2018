# https://adventofcode.com/2018/day/14


def part2(input_file):
	with open(input_file, "r") as f:
		score_sequence = f.read().strip()

	target = [int(c) for c in score_sequence]
	target_len = len(target)

	recipes = [3, 7]
	pos1, pos2 = 0, 1

	def matches_at_end(offset):
		end = len(recipes) - offset
		return recipes[end - target_len:end] == target

	while True:
		total = recipes[pos1] + recipes[pos2]

		if total >= 10:
			recipes.append(total // 10)
			if matches_at_end(0):
				return len(recipes) - target_len

		recipes.append(total % 10)
		if matches_at_end(0):
			return len(recipes) - target_len

		pos1 = (pos1 + 1 + recipes[pos1]) % len(recipes)
		pos2 = (pos2 + 1 + recipes[pos2]) % len(recipes)


def main():
	input_file = "day14-input.txt"
	print(part2(input_file))


if __name__ == "__main__":
	main()
