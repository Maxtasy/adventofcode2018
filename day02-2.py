# https://adventofcode.com/2018/day/2

def find_common_letters(input_file):
	with open(input_file, "r") as f:
		box_ids = f.read().strip().split()

	for i in range(len(box_ids) - 1):
		for j in range(i, len(box_ids) - 1):
			difference = 0

			for k in range(len(box_ids[i])):
				if box_ids[i][k] != box_ids[j][k]:
					difference += 1
					pos = k

				if difference > 1:
					break

			if difference == 1:
				common_letters = box_ids[i][:pos] + box_ids[i][pos + 1:]
				return common_letters

	return None


def main():
	input_file = "day02-input.txt"
	print(find_common_letters(input_file))


if __name__ == "__main__":
	main()