# https://adventofcode.com/2018/day/14


def part1(input_file):
	with open(input_file, "r") as f:
		recipe_count = int(f.read())

	pos1 = 0
	pos2 = 1

	recipes = [3, 7]

	while len(recipes) < recipe_count + 10:
		new_recipe = str(recipes[pos1] + recipes[pos2])

		for i in range(len(new_recipe)):
			recipes.append(int(new_recipe[i]))

		move1 = 1 + recipes[pos1]
		move2 = 1 + recipes[pos2]

		pos1 = (pos1 + move1) % len(recipes)
		pos2 = (pos2 + move2) % len(recipes)

	scores = recipes[-10:]
	scores = list(map(str, scores))

	return "".join(scores)


def main():
	input_file = "day14-input.txt"
	print(part1(input_file))


if __name__ == "__main__":
	main()