# https://adventofcode.com/2018/day/22

import heapq

NEITHER, TORCH, CLIMBING = 0, 1, 2

# Region type -> the two tools usable there.
ALLOWED_TOOLS = {
	0: {TORCH, CLIMBING},  # rocky
	1: {NEITHER, CLIMBING},  # wet
	2: {NEITHER, TORCH},  # narrow
}


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


def part2(input_file):
	depth, target = parse(input_file)
	erosion_level = make_erosion_level(depth, target)

	def region_type(x, y):
		return erosion_level(x, y) % 3

	start = (0, 0, TORCH)
	goal = (target[0], target[1], TORCH)

	best = {start: 0}
	pq = [(0, start)]

	while pq:
		time, state = heapq.heappop(pq)
		if state == goal:
			return time
		if time > best.get(state, float("inf")):
			continue

		x, y, tool = state

		# Switch tools in place.
		for other_tool in ALLOWED_TOOLS[region_type(x, y)]:
			if other_tool != tool:
				new_state = (x, y, other_tool)
				new_time = time + 7
				if new_time < best.get(new_state, float("inf")):
					best[new_state] = new_time
					heapq.heappush(pq, (new_time, new_state))

		# Move to an adjacent region, if the current tool is usable there.
		for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
			nx, ny = x + dx, y + dy
			if nx < 0 or ny < 0:
				continue
			if tool not in ALLOWED_TOOLS[region_type(nx, ny)]:
				continue
			new_state = (nx, ny, tool)
			new_time = time + 1
			if new_time < best.get(new_state, float("inf")):
				best[new_state] = new_time
				heapq.heappush(pq, (new_time, new_state))

	raise RuntimeError("no path found")


def main():
	input_file = "day22-input.txt"
	print(part2(input_file))


if __name__ == "__main__":
	main()
