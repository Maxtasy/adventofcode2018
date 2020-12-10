# https://adventofcode.com/2018/day/1

def calculate_end_frequency(input_file):
	with open(input_file, "r") as f:
		changes = f.read().strip().split()
		changes = map(int, changes)

	return sum(changes)


def main():
	input_file = "day01-input.txt"
	print(calculate_end_frequency(input_file))


if __name__ == "__main__":
	main()