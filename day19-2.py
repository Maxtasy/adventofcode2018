# https://adventofcode.com/2018/day/19

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


def run(ip_register, program, registers, max_steps):
	ip = 0
	steps = 0
	while 0 <= ip < len(program) and steps < max_steps:
		registers[ip_register] = ip
		op, a, b, c = program[ip]
		registers[c] = OPS[op](registers, a, b)
		ip = registers[ip_register] + 1
		steps += 1
	return registers


def sum_of_divisors(n):
	total = 0
	i = 1
	while i * i <= n:
		if n % i == 0:
			total += i
			if i != n // i:
				total += n // i
		i += 1
	return total


def part2(input_file):
	ip_register, program = parse(input_file)
	# Same shortcut as part 1: let the program finish setting up its target
	# number with register 0 initialized to 1, then compute the divisor sum
	# directly instead of running the slow in-program loop to completion.
	registers = run(ip_register, program, [1, 0, 0, 0, 0, 0], max_steps=200)
	n = max(registers)
	return sum_of_divisors(n)


def main():
	input_file = "day19-input.txt"
	print(part2(input_file))


if __name__ == "__main__":
	main()
