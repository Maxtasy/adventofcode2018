# https://adventofcode.com/2018/day/3

def find_total_shared_squares(input_file):
	with open(input_file, "r") as f:
		lines = f.read().strip().split("\n")

		claims = []

		for line in lines:
			line = line.replace("#", "").replace("@", "").replace(":", "").replace(",", " ").replace("x", " ").split()
			claims.append([int(line[1]), int(line[2]), int(line[3]), int(line[4])]) 
			
		squares = {}

		for claim_id, claim in enumerate(claims):
			for w in range(claim[0], claim[0] + claim[2]):
				for h in range(claim[1], claim[1] + claim[3]):
					if (w, h) not in squares.keys():
						squares[(w, h)] = []
					squares[(w, h)].append(claim_id)

		shared_squares = 0

		for square in squares:
			if len(squares[square]) > 1:
				shared_squares += 1

	return shared_squares


def main():
	input_file = "day03-input.txt"
	print(find_total_shared_squares(input_file))


if __name__ == "__main__":
	main()