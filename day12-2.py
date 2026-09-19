# https://adventofcode.com/2018/day/12

TARGET_GENERATION = 50_000_000_000


def nextg(cur, recipe):
	start = min(cur)
	end = max(cur)
	x = set()

	for i in range(start - 3, end + 4):
		pat = ''.join('#' if i + k in cur else '.' for k in [-2, -1, 0, 1, 2])
		if pat in recipe:
			x.add(i)

	return x


def part2(input_file):
	with open(input_file) as f:
		lines = [l.rstrip('\n') for l in f]

	init = lines[0][len('initial state: '):]
	recipe = set()
	for l in lines[2:]:
		if l[-1] == '#':
			recipe.add(l[:5])

	cur = set(i for i, c in enumerate(init) if c == '#')

	last_sum = sum(cur)
	last_delta = None
	generation = 0

	# Run until the sum-of-pot-numbers delta between generations stabilizes
	# (two consecutive equal deltas), then extrapolate linearly to the target.
	while generation < TARGET_GENERATION:
		cur = nextg(cur, recipe)
		generation += 1
		current_sum = sum(cur)
		delta = current_sum - last_sum
		last_sum = current_sum

		if delta == last_delta:
			return current_sum + (TARGET_GENERATION - generation) * delta

		last_delta = delta

	return last_sum


def main():
	input_file = "day12-input.txt"
	print(part2(input_file))


if __name__ == "__main__":
	main()
