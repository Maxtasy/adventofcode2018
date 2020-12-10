# https://adventofcode.com/2018/day/1

def find_duplicate_frequency(input_file):
	with open(input_file, "r") as f:
		changes = f.read().strip().split()

	frequency = 0
	frequency_list = [0,]

	duplicate_found = False
	
	while not duplicate_found:
		for change in changes:
			if change[0] == "+":
				frequency += int(change[1:])
			else:
				frequency -= int(change[1:])

			if frequency in frequency_list:
				duplicate_found = True
				break;
			else:
				frequency_list.append(frequency)

			print("running", len(frequency_list))

	return frequency


def main():
	input_file = "day01-input.txt"
	print(find_duplicate_frequency(input_file))


if __name__ == "__main__":
	main()