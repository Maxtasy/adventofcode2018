# https://adventofcode.com/2018/day/21

OPS = {
	"addr": lambda r, a, b: r[a] + r[b],
	"addi": lambda r, a, b: r[a] + b,
	"mulr": lambda r, a, b: r[a] * r[b],
	"muli": lambda r, a, b: r[a] * b,
	"banr": lambda r, a, b: r[a] & r[b],
	"bani": lambda r, a, b: r[a] & b,
	"borr": lambda r, a, b: r[a] | r[b],
	"bori": lambda r, a, b: r[a] | b,
	"setr": lambda r, a, b: r[a],
	"seti": lambda r, a, b: a,
	"gtir": lambda r, a, b: 1 if a > r[b] else 0,
	"gtri": lambda r, a, b: 1 if r[a] > b else 0,
	"gtrr": lambda r, a, b: 1 if r[a] > r[b] else 0,
	"eqir": lambda r, a, b: 1 if a == r[b] else 0,
	"eqri": lambda r, a, b: 1 if r[a] == b else 0,
	"eqrr": lambda r, a, b: 1 if r[a] == r[b] else 0,
}


def parse(input_file):
	with open(input_file) as f:
		lines = f.read().strip().split("\n")

	ip_register = int(lines[0].split()[1])
	program = []
	for line in lines[1:]:
		parts = line.split()
		program.append((parts[0], int(parts[1]), int(parts[2]), int(parts[3])))

	return ip_register, program


def find_target_register(program):
	# The only instruction that ever reads register 0 is the eqrr that
	# decides whether to halt; the other operand is the value the program
	# is effectively comparing r0 against.
	for op, a, b, c in program:
		if op == "eqrr" and (a == 0 or b == 0):
			return b if a == 0 else a
	raise ValueError("no eqrr instruction referencing register 0 found")


def first_halting_value(input_file):
	ip_register, program = parse(input_file)
	target_register = find_target_register(program)

	registers = [0, 0, 0, 0, 0, 0]
	ip = 0
	while 0 <= ip < len(program):
		registers[ip_register] = ip
		op, a, b, c = program[ip]
		if op == "eqrr" and (a == target_register or b == target_register) and (a == 0 or b == 0):
			return registers[target_register]
		registers[c] = OPS[op](registers, a, b)
		ip = registers[ip_register] + 1

	raise RuntimeError("program halted without reaching the comparison")


def part1(input_file):
	return first_halting_value(input_file)


def main():
	input_file = "day21-input.txt"
	print(part1(input_file))


if __name__ == "__main__":
	main()
