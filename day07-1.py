# https://adventofcode.com/2018/day/7

def part1(input_file):
	with open(input_file, "r") as f:
		lines = f.read().strip().split("\n")

	switches = {}
	default_on = ["E", "P", "X"]

	for default in default_on:
		switches[default] = [0, []]

	for line in lines:
		parts = line.split()
		switch = parts[7]
		dependency = parts[1]
		if switch not in switches:
			switches[switch] = [0,[]]
		switches[switch][1].append(dependency)

	order = ""

	while True:
		available = []

		for switch in switches:
			if switch not in order:
				possible = True
				if len(switches[switch][1]) > 0:
					for dependency in switches[switch][1]: 
						if not switches[dependency][0]:
							possible = False
							break
				if possible:
					available.append(switch)

		if len(available) < 1:
			break

		current = min(available)
		order += current
		switches[current][0] = 1

	return order

def main():
	input_file = "day07-input.txt"
	print(part1(input_file))

if __name__ == "__main__":
	main()