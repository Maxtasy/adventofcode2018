# https://adventofcode.com/2018/day/22


def parse(input_file):
	with open(input_file) as f:
		lines = f.read().strip().split("\n")

	depth = int(lines[0].split(": ")[1])
	tx, ty = (int(v) for v in lines[1].split(": ")[1].split(","))

	return depth, (tx, ty)


def make_erosion_level(depth, target):
	cache = {}

	def geologic_index(x, y):
		if (x, y) == (0, 0) or (x, y) == target:
			return 0
		if y == 0:
			return x * 16807
		if x == 0:
			return y * 48271
		return erosion_level(x - 1, y) * erosion_level(x, y - 1)

	def erosion_level(x, y):
		if (x, y) not in cache:
			cache[(x, y)] = (geologic_index(x, y) + depth) % 20183
		return cache[(x, y)]

	return erosion_level


def region_type(erosion_level, x, y):
	return erosion_level(x, y) % 3


def part1(input_file):
	depth, target = parse(input_file)
	erosion_level = make_erosion_level(depth, target)

	total = 0
	for y in range(target[1] + 1):
		for x in range(target[0] + 1):
			total += region_type(erosion_level, x, y)

	return total


def main():
	input_file = "day22-input.txt"
	print(part1(input_file))


if __name__ == "__main__":
	main()
