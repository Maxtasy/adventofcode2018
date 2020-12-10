# https://adventofcode.com/2018/day/2

def calculate_checksum(input_file):
	with open(input_file, "r") as f:
		box_ids = f.read().strip().split()

	total_doubles = 0
	total_triples = 0

	for box_id in box_ids:
		singles = []
		doubles = []
		triples = []
		ignored = []

		for letter in box_id:
			if letter in ignored:
				continue
			elif letter in triples:
				triples.remove(letter)
				ignored.append(letter)
			elif letter in doubles:
				doubles.remove(letter)
				triples.append(letter)
			elif letter in singles:
				singles.remove(letter)
				doubles.append(letter)
			else:
				singles.append(letter)

		if len(doubles) >= 1:
			total_doubles += 1

		if len(triples) >= 1:
			total_triples += 1

	checksum = total_triples * total_doubles

	return checksum


def main():
	input_file = "day02-input.txt"
	print(calculate_checksum(input_file))


if __name__ == "__main__":
	main()