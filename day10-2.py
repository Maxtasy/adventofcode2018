# https://adventofcode.com/2018/day/10

def parse_points(input_file):
	with open(input_file, "r") as f:
		lines = f.read().strip().split("\n")

	points = []

	for line in lines:
		line = line.replace("position=<", "").replace("velocity=<", "")
		parts = line.split()
		x = int(parts[0][:-1])
		y = int(parts[1][:-1])
		x_vel = int(parts[2][:-1])
		y_vel = int(parts[3][:-1])
		points.append([x, y, x_vel, y_vel])

	return points


def bbox_area(points, t):
	xs = [p[0] + p[2] * t for p in points]
	ys = [p[1] + p[3] * t for p in points]
	return (max(xs) - min(xs)) * (max(ys) - min(ys))


def find_convergence_second(points):
	# The message is legible when the points' bounding box is smallest.
	# Bounding box area shrinks then grows again, so scan until it starts increasing.
	t = 0
	while bbox_area(points, t + 1) < bbox_area(points, t):
		t += 1
	return t


def part2(input_file):
	points = parse_points(input_file)
	return find_convergence_second(points)


def main():
	input_file = "day10-input.txt"
	print(part2(input_file))

if __name__ == "__main__":
	main()
