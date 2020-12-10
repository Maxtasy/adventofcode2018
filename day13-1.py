# https://adventofcode.com/2018/day/13


def part1(input_file):	
	with open(input_file, "r") as f:
		lines = f.read().strip("\n").split("\n")

	dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
	next_turn = [-1, 0, 1]

	tracks = {}

	# Carts have properties: position as (x, y), direction as (dir_x, dir_y) and next crossing turn as 0, 1 or 2 for left, straight, right
	carts = []

	for y in range(len(lines)):
		for x in range(len(lines[0])):
			if lines[y][x] == "<":
				tracks[(y, x)] = "-"
				carts.append([(y, x), (0, -1), -1])
			elif lines[y][x] == ">":
				tracks[(y, x)] = "-"
				carts.append([(y, x), (0, 1), -1])
			elif lines[y][x] == "^":
				tracks[(y, x)] = "|"
				carts.append([(y, x), (-1, 0), -1])
			elif lines[y][x] == "v":
				tracks[(y, x)] = "|"
				carts.append([(y, x), (1, 0), -1])
			else:
				tracks[(y, x)] = lines[y][x]

	ticks = 0

	while True:
		carts.sort()

		cart_positions = []

		for cart in carts:
			cart_positions.append(cart[0])

		for cart in carts:
			cart[0] = (cart[0][0] + cart[1][0], cart[0][1] + cart[1][1])

			if cart[0] in cart_positions:
				return str(cart[0][1]) + "," + str(cart[0][0])
			elif tracks[cart[0]] == "+":
				cart[1] = dirs[(dirs.index(cart[1]) + cart[2]) % 4]
				cart[2] = next_turn[(next_turn.index(cart[2]) + 1) % 3]
			elif tracks[cart[0]] == "\\":
				if cart[1] == (1, 0) or cart[1] == (-1, 0):
					cart[1] = dirs[(dirs.index(cart[1]) - 1) % 4]
				elif cart[1] == (0, 1) or cart[1] == (0, -1):
					cart[1] = dirs[(dirs.index(cart[1]) + 1) % 4]
			elif tracks[cart[0]] == "/":
				if cart[1] == (0, 1) or cart[1] == (0, -1):
					cart[1] = dirs[(dirs.index(cart[1]) - 1) % 4]
				elif cart[1] == (1, 0) or cart[1] == (-1, 0):
					cart[1] = dirs[(dirs.index(cart[1]) + 1) % 4]
		
		ticks += 1


def main():
	input_file = "day13-input.txt"
	print(part1(input_file))


if __name__ == "__main__":
	main()