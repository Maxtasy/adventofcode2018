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


def part1(input_file):
	points = parse_points(input_file)
	seconds = find_convergence_second(points)

	for point in points:
		point[0] += point[2] * seconds
		point[1] += point[3] * seconds

	smallest_x = min(point[0] for point in points)
	smallest_y = min(point[1] for point in points)
	biggest_x = max(point[0] for point in points)
	biggest_y = max(point[1] for point in points)

	occupied = {(point[1], point[0]) for point in points}

	rows = []
	for row in range(smallest_y, biggest_y + 1):
		rows.append("".join("#" if (row, col) in occupied else "." for col in range(smallest_x, biggest_x + 1)))

	return "\n".join(rows)


def main():
	input_file = "day10-input.txt"
	print(part1(input_file))

if __name__ == "__main__":
	main()
