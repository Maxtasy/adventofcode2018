# https://adventofcode.com/2018/day/17

import sys
import threading


def parse_clay(input_file):
	clay = set()
	with open(input_file) as f:
		for line in f:
			line = line.strip()
			if not line:
				continue
			a, b = line.split(", ")
			k1, v1 = a.split("=")
			k2, rng = b.split("=")
			v2a, v2b = (int(v) for v in rng.split(".."))
			if k1 == "x":
				x = int(v1)
				for y in range(v2a, v2b + 1):
					clay.add((x, y))
			else:
				y = int(v1)
				for x in range(v2a, v2b + 1):
					clay.add((x, y))
	return clay


def flood(clay, max_y):
	tiles = {}

	def is_solid(x, y):
		return (x, y) in clay or tiles.get((x, y)) == "~"

	def fill(x, y):
		if y > max_y:
			return
		if (x, y) in tiles or (x, y) in clay:
			return

		tiles[(x, y)] = "|"
		if y == max_y:
			return

		fill(x, y + 1)

		if is_solid(x, y + 1):
			left_x, left_wall = scan(x, y, -1)
			right_x, right_wall = scan(x, y, 1)

			if left_wall and right_wall:
				for xi in range(left_x, right_x + 1):
					tiles[(xi, y)] = "~"
			else:
				for xi in range(left_x, right_x + 1):
					tiles[(xi, y)] = "|"

	def scan(x, y, dx):
		cx = x
		while True:
			nx = cx + dx
			if (nx, y) in clay:
				return cx, True
			fill(nx, y + 1)
			if not is_solid(nx, y + 1):
				return nx, False
			cx = nx

	fill(500, 0)
	return tiles


def part2(input_file):
	clay = parse_clay(input_file)
	min_y = min(y for x, y in clay)
	max_y = max(y for x, y in clay)

	tiles = flood(clay, max_y)

	return sum(1 for (x, y), v in tiles.items() if min_y <= y <= max_y and v == "~")


def main():
	input_file = "day17-input.txt"
	print(part2(input_file))


def run():
	sys.setrecursionlimit(1_000_000)
	main()


if __name__ == "__main__":
	threading.stack_size(64 * 1024 * 1024)
	t = threading.Thread(target=run)
	t.start()
	t.join()
