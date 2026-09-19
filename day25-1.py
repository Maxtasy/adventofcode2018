# https://adventofcode.com/2018/day/25


def manhattan(a, b):
	return sum(abs(x - y) for x, y in zip(a, b))


class UnionFind:
	def __init__(self, n):
		self.parent = list(range(n))

	def find(self, i):
		while self.parent[i] != i:
			self.parent[i] = self.parent[self.parent[i]]
			i = self.parent[i]
		return i

	def union(self, a, b):
		ra, rb = self.find(a), self.find(b)
		if ra != rb:
			self.parent[ra] = rb


def part1(input_file):
	with open(input_file) as f:
		points = [tuple(int(v) for v in line.strip().split(",")) for line in f if line.strip()]

	uf = UnionFind(len(points))
	for i in range(len(points)):
		for j in range(i + 1, len(points)):
			if manhattan(points[i], points[j]) <= 3:
				uf.union(i, j)

	return len(set(uf.find(i) for i in range(len(points))))


def main():
	input_file = "day25-input.txt"
	print(part1(input_file))


if __name__ == "__main__":
	main()
