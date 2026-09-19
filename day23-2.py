# https://adventofcode.com/2018/day/23

import heapq


def parse(input_file):
	bots = []
	with open(input_file) as f:
		for line in f:
			line = line.strip()
			pos_part, r_part = line.split(", r=")
			x, y, z = (int(v) for v in pos_part[len("pos=<"):-1].split(","))
			bots.append((x, y, z, int(r_part)))
	return bots


def min_distance_to_point(box, point):
	x0, y0, z0, size = box
	dist = 0
	for c, p in zip((x0, y0, z0), point):
		if p < c:
			dist += c - p
		elif p > c + size - 1:
			dist += p - (c + size - 1)
	return dist


def bots_in_range(box, bots):
	return sum(1 for (x, y, z, r) in bots if min_distance_to_point(box, (x, y, z)) <= r)


def part2(input_file):
	bots = parse(input_file)

	min_coord = min(min(x, y, z) for x, y, z, r in bots)
	max_coord = max(max(x, y, z) for x, y, z, r in bots)

	size = 1
	while size < (max_coord - min_coord + 1):
		size *= 2

	start = (min_coord, min_coord, min_coord, size)
	heap = [(-bots_in_range(start, bots), size, 0, start)]

	while heap:
		neg_count, box_size, dist_to_origin, box = heapq.heappop(heap)

		if box_size == 1:
			return dist_to_origin

		x0, y0, z0, _ = box
		half = box_size // 2
		for dx in (0, half):
			for dy in (0, half):
				for dz in (0, half):
					sub = (x0 + dx, y0 + dy, z0 + dz, half)
					count = bots_in_range(sub, bots)
					dist = min_distance_to_point(sub, (0, 0, 0))
					heapq.heappush(heap, (-count, half, dist, sub))

	raise RuntimeError("search exhausted without finding a point")


def main():
	input_file = "day23-input.txt"
	print(part2(input_file))


if __name__ == "__main__":
	main()
