# https://adventofcode.com/2018/day/1

def find_duplicate_frequency(input_file):
	with open(input_file, "r") as f:
		changes = f.read().strip().split()

	frequency = 0
	seen = {0}

	duplicate_found = False

	while not duplicate_found:
		for change in changes:
			if change[0] == "+":
				frequency += int(change[1:])
			else:
				frequency -= int(change[1:])

			if frequency in seen:
				duplicate_found = True
				break
			else:
				seen.add(frequency)

	return frequency


def main():
	input_file = "day01-input.txt"
	print(find_duplicate_frequency(input_file))


if __name__ == "__main__":
	main()