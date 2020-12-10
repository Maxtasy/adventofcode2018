# https://adventofcode.com/2018/day/10

def part1(input_file):
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

	# We start at 0 seconds
	seconds = 0
	smallest = None

	while seconds < 10391:
		smallest_x = None
		smallest_y = None
		biggest_x = None
		biggest_y = None

		for point in points:
			point[0] += point[2]
			point[1] += point[3]

			# Find smallest x value (left side of rectangle)
			if smallest_x == None:
				smallest_x = point[0]
			else:
				smallest_x = min(smallest_x, point[0])

			# Find smallest y value (bottom side of rectangle)
			if smallest_y == None:
				smallest_y = point[1]
			else:
				smallest_y = min(smallest_y, point[1])

			# Find biggest x value (left side of rectangle)
			if biggest_x == None:
				biggest_x = point[0]
			else:
				biggest_x = max(biggest_x, point[0])

			# Find biggest y value (left side of rectangle)
			if biggest_y == None:
				biggest_y = point[1]
			else:
				biggest_y = max(biggest_y, point[1])

		# 1 second passed while all points moved to their new positions
		seconds += 1

	print("Code is shown at " + str(seconds) + " seconds.")

	# Build matrix so we can draw all points
	matrix = {}

	for row in range(smallest_y, biggest_y + 1):
		for col in range(smallest_x, biggest_x + 1):
			matrix[(row, col)] = "."
		matrix[(row, col + 1)] = "\n"
	
	for point in points:
		matrix[(point[1], point[0])] = "#"

	s = ""

	for row in range(smallest_y, biggest_y + 1):
		for col in range(smallest_x, biggest_x + 2):
			s += matrix[(row, col)]

	print(s)


def main():
	input_file = "day10-input.txt"
	part1(input_file)

if __name__ == "__main__":
	main()