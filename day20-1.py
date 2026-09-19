# https://adventofcode.com/2018/day/20

from collections import deque

DIRS = {"N": (0, -1), "S": (0, 1), "E": (1, 0), "W": (-1, 0)}


def build_doors(regex):
	doors = set()
	current = {(0, 0)}

	branch_start_stack = []
	branch_ends_stack = []

	for ch in regex:
		if ch in "^$":
			continue
		elif ch in DIRS:
			dx, dy = DIRS[ch]
			new_current = set()
			for (x, y) in current:
				nx, ny = x + dx, y + dy
				doors.add(frozenset({(x, y), (nx, ny)}))
				new_current.add((nx, ny))
			current = new_current
		elif ch == "(":
			branch_start_stack.append(current)
			branch_ends_stack.append(set())
		elif ch == "|":
			branch_ends_stack[-1] |= current
			current = branch_start_stack[-1]
		elif ch == ")":
			branch_ends_stack[-1] |= current
			current = branch_ends_stack.pop()
			branch_start_stack.pop()

	return doors


def compute_distances(doors):
	adjacency = {}
	for edge in doors:
		a, b = tuple(edge)
		adjacency.setdefault(a, set()).add(b)
		adjacency.setdefault(b, set()).add(a)

	distances = {(0, 0): 0}
	q = deque([(0, 0)])
	while q:
		pos = q.popleft()
		for neighbour in adjacency.get(pos, ()):
			if neighbour not in distances:
				distances[neighbour] = distances[pos] + 1
				q.append(neighbour)

	return distances


def part1(input_file):
	with open(input_file) as f:
		regex = f.read().strip()

	doors = build_doors(regex)
	distances = compute_distances(doors)

	return max(distances.values())


def main():
	input_file = "day20-input.txt"
	print(part1(input_file))


if __name__ == "__main__":
	main()
