# https://adventofcode.com/2018/day/18

TARGET_MINUTES = 1_000_000_000


def step(grid, width, height):
	new_grid = []
	for y in range(height):
		row = []
		for x in range(width):
			neighbours = [
				grid[ny][nx]
				for ny in range(max(0, y - 1), min(height, y + 2))
				for nx in range(max(0, x - 1), min(width, x + 2))
				if (nx, ny) != (x, y)
			]
			c = grid[y][x]
			if c == ".":
				row.append("|" if neighbours.count("|") >= 3 else ".")
			elif c == "|":
				row.append("#" if neighbours.count("#") >= 3 else "|")
			else:
				if neighbours.count("#") >= 1 and neighbours.count("|") >= 1:
					row.append("#")
				else:
					row.append(".")
		new_grid.append(row)
	return new_grid


def score(grid):
	wooded = sum(row.count("|") for row in grid)
	lumberyards = sum(row.count("#") for row in grid)
	return wooded * lumberyards


def part2(input_file):
	with open(input_file) as f:
		grid = [list(line) for line in f.read().strip().split("\n")]

	height = len(grid)
	width = len(grid[0])

	seen = {}
	scores = []

	minute = 0
	while minute < TARGET_MINUTES:
		key = tuple(tuple(row) for row in grid)
		if key in seen:
			cycle_start = seen[key]
			cycle_len = minute - cycle_start
			remaining = (TARGET_MINUTES - minute) % cycle_len
			return scores[cycle_start + remaining]

		seen[key] = minute
		scores.append(score(grid))

		grid = step(grid, width, height)
		minute += 1

	return score(grid)


def main():
	input_file = "day18-input.txt"
	print(part2(input_file))


if __name__ == "__main__":
	main()
