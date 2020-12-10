# https://adventofcode.com/2018/day/14


def part2(input_file):
	with open(input_file, "r") as f:
		score_sequence = f.read()

	pos1 = 0
	pos2 = 1

	recipes = "37"

	# We make -7 because it might add 2 numbers at the end so we have to check a range of 7 instead of 6
	while score_sequence not in recipes[-7:]:
		new_recipe = str(int(recipes[pos1]) + int(recipes[pos2]))

		recipes += new_recipe

		move1 = 1 + int(recipes[pos1])
		move2 = 1 + int(recipes[pos2])

		pos1 = (pos1 + move1) % len(recipes)
		pos2 = (pos2 + move2) % len(recipes)

	return recipes.index(score_sequence)


def main():
	input_file = "day14-input.txt"
	print(part2(input_file))


if __name__ == "__main__":
	main()