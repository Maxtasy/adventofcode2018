# https://adventofcode.com/2018/day/3

def find_unshared_claim(input_file):
	with open(input_file, "r") as f:
		lines = f.read().strip().split("\n")

		claims = []

		for line in lines:
			line = line.replace("#", "").replace("@", "").replace(":", "").replace(",", " ").replace("x", " ").split()
			claims.append([int(line[1]), int(line[2]), int(line[3]), int(line[4])]) 
		
		unshared_claims = []

		# Populate squares with claims
		squares = {}

		for claim_id, claim in enumerate(claims, start=1):
			for w in range(claim[0], claim[0] + claim[2]):
				for h in range(claim[1], claim[1] + claim[3]):
					if (w, h) not in squares.keys():
						squares[(w, h)] = []
					squares[(w, h)].append(claim_id)

		# Iterate over each claim
		for claim_id, claim in enumerate(claims, start=1):
			# Set possible flag to true
			possible = True
			# Iterate over the whole width of the claim
			for w in range(claim[0], claim[0] + claim[2]):
				# Iterate over the whole height of the claim
				for h in range(claim[1], claim[1] + claim[3]):
					# If the current square has not exactly 1 owner we set possible to false and break
					if claim_id not in squares[(w, h)] or len(squares[(w, h)]) > 1:
						possible = False
						break
				# If possible flag is set to false we can also skip all other squares, so we break
				if not possible:
					break
			# If all squares of the current claim passed the check, we found our claim and can return the claim_id
			if possible:
				return claim_id
		# If none of the claims passed the check we return None
		return None


def main():
	input_file = "day03-input.txt"
	print(find_unshared_claim(input_file))


if __name__ == "__main__":
	main()