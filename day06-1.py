# https://adventofcode.com/2018/day/6

def largest_area_size(input_file):

	# Returns Manhatten Distance between two x/y coordinate tuples
	def calc_man_dist(coord_1, coord_2):
		dist_x = abs(coord_1[0] - coord_2[0])
		dist_y = abs(coord_1[1] - coord_2[1])

		return dist_x + dist_y


	with open(input_file, "r") as f:
		lines = f.read().strip().split("\n")

	max_x = 0
	max_y = 0

	# Dictionary of main points. keys 1-50, values = (x, y) tuple of coordinates
	main_points = {}

	for point_id, line in enumerate(lines, start=1):
		x, y = map(int, line.split(", "))

		max_x = max(max_x, x)
		max_y = max(max_y, y)

		main_points[point_id] = (x, y)

	#print(main_points)

	# Dictionary with area sizes for each main point, initialized as 0
	area_sizes = {}

	for i in range(1, 51):
		area_sizes[i] = 0


	infinite_ids = set()


	# Iterate over all coordinates and add 1 to the area size of main points whenever a coordinate is closest to it (unique)
	for x in range(max_x + 1):
		for y in range(max_y + 1):
			shortest = max_x + max_y
			multiple = False

			for main_point in main_points:
				distance = calc_man_dist((x, y), main_points[main_point])

				if distance < shortest:
					shortest = distance
					owner = main_point
					multiple = False
				elif distance == shortest:
					multiple = True

			if not multiple:
				area_sizes[owner] += 1

				if x == 0 or x == max_x or y == 0 or y == max_y:
					infinite_ids.add(owner)


	return max(size for coord_id, size in area_sizes.items() if coord_id not in infinite_ids)


def main():
	input_file = "day06-input.txt"
	print(largest_area_size(input_file))


if __name__ == "__main__":
	main()