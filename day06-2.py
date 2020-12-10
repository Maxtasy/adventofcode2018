# https://adventofcode.com/2018/day/6

def part2(input_file, manhattan_limit=10000):
	with open(input_file, "r") as f:
		lines = f.read().strip().split("\n")
	
	coords = set()
	max_r = max_c = 0

	for line in lines:
		r, c = map(int, line.split(", "))
		coords.add((r, c))
		max_r = max(max_r, r)
		max_c = max(max_c, c)

	size_shared_region = 0

	for i in range(max_r + 1):
		for j in range(max_c + 1):
			size_shared_region += int(sum(abs(r - i) + abs(c - j) for r, c in coords) < manhattan_limit)

	return size_shared_region


def main():
	input_file = "day06-input.txt"
	print(part2(input_file))


if __name__ == "__main__":
	main()