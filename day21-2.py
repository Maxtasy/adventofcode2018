# https://adventofcode.com/2018/day/21


def parse(input_file):
	with open(input_file) as f:
		lines = f.read().strip().split("\n")

	program = []
	for line in lines[1:]:
		parts = line.split()
		program.append((parts[0], int(parts[1]), int(parts[2]), int(parts[3])))

	return program


def find_target_register(program):
	for op, a, b, c in program:
		if op == "eqrr" and (a == 0 or b == 0):
			return b if a == 0 else a
	raise ValueError("no eqrr instruction referencing register 0 found")


def extract_magic_number(input_file):
	# All day 21 programs follow the same "hash loop" shape; the target
	# register is reset with a large seed inside the loop. It also gets a
	# small decoy constant (123) in an unrelated one-time preamble check, so
	# take the largest seti value written to it.
	program = parse(input_file)
	target_register = find_target_register(program)

	candidates = [a for op, a, b, c in program if op == "seti" and c == target_register]
	return max(candidates)


def part2(input_file):
	magic = extract_magic_number(input_file)

	r3 = 0
	seen = set()
	last_value = None

	while True:
		r1 = r3 | 65536
		r3 = magic
		while True:
			r3 = ((r3 + (r1 & 255)) & 16777215) * 65899 & 16777215
			if r1 < 256:
				break
			r1 //= 256

		if r3 in seen:
			return last_value
		seen.add(r3)
		last_value = r3


def main():
	input_file = "day21-input.txt"
	print(part2(input_file))


if __name__ == "__main__":
	main()
