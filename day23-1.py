# https://adventofcode.com/2018/day/23


def parse(input_file):
	bots = []
	with open(input_file) as f:
		for line in f:
			line = line.strip()
			pos_part, r_part = line.split(", r=")
			x, y, z = (int(v) for v in pos_part[len("pos=<"):-1].split(","))
			bots.append((x, y, z, int(r_part)))
	return bots


def manhattan(a, b):
	return abs(a[0] - b[0]) + abs(a[1] - b[1]) + abs(a[2] - b[2])


def part1(input_file):
	bots = parse(input_file)
	strongest = max(bots, key=lambda b: b[3])
	sx, sy, sz, sr = strongest

	return sum(1 for (x, y, z, r) in bots if manhattan((x, y, z), (sx, sy, sz)) <= sr)


def main():
	input_file = "day23-input.txt"
	print(part1(input_file))


if __name__ == "__main__":
	main()
