# https://adventofcode.com/2018/day/13


from itertools import product


def part2(input_file):	
	with open(input_file, 'r') as f:
		rlmap = [list(line.strip('\n')) for line in f]
		
	carts = []

	for y, x in product(range(len(rlmap)), range(len(rlmap[0]))):
		if rlmap[y][x] in '>v<^':
			crdir = '>v<^'.index(rlmap[y][x])
			rlmap[y][x] = '-|'[crdir & 1]
			carts.append([y, x, crdir, 0, True])

	crash = False

	while len(carts) > 1:
		carts.sort(key=lambda i: tuple(i[:2]))
		for cart1 in carts:
			if not cart1[-1]:
				continue
			if rlmap[cart1[0]][cart1[1]] == '/':
				cart1[2] = (3, 2, 1, 0)[cart1[2]]
			elif rlmap[cart1[0]][cart1[1]] == '\\':
				cart1[2] = (1, 0, 3, 2)[cart1[2]]
			elif rlmap[cart1[0]][cart1[1]] == '+':
				cart1[2] = (cart1[2] + (-1, 0, 1)[cart1[3]]) & 3
				cart1[3] = (cart1[3] + 1) % 3
			cart1[0] += (0, 1, 0, -1)[cart1[2]]
			cart1[1] += (1, 0, -1, 0)[cart1[2]]
			for cart2 in carts:
				if cart2[-1] and cart1 is not cart2 and cart1[:2] == cart2[:2]:
					cart1[-1] = cart2[-1] = False
		carts = list(filter(lambda i: i[-1], carts))

	return str(carts[0][1]) + "," + str(carts[0][0])


def main():
	input_file = "day13-input.txt"
	print(part2(input_file))


if __name__ == "__main__":
	main()