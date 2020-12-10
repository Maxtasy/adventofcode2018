# https://adventofcode.com/2018/day/11

def part1(grid_serial_number, size):
	fuel_cells = {}

	for y in range(1, size + 1):
		for x in range(1, size + 1):
			rack_id = x + 10
			power_level = (rack_id * y + grid_serial_number) * rack_id
			if len(str(power_level)) < 3:
				power_level = 0
			else:
				power_level = int(str(power_level)[-3])

			power_level -= 5

			fuel_cells[(x, y)] = power_level

	square_power = {}
	most_power = 0

	for y in range(1, size + 1 - 2):
		for x in range(1, size + 1 - 2):
			power_total = 0

			for i in range(3):
				for j in range(3):
					power_total += fuel_cells[(x + i, y + j)]

			square_power[(x, y)] = power_total

			if power_total > most_power:
				most_power = power_total
				best_square_x = x
				best_square_y = y

	result = str(best_square_x) + "," + str(best_square_y)

	return result


def main():
	grid_serial_number = int(open("day11-input.txt").read())
	size = 300
	print(part1(grid_serial_number, size))


if __name__ == "__main__":
	main()