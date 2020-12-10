# https://adventofcode.com/2018/day/4

def solve(input_file):
	with open(input_file, "r") as f:
		lines = f.read().strip().split("\n")

	lines.sort()

	sleep_data = {}

	for line in lines:
		log = line.split()

		if "Guard" in log:
			current_guard = int(log[3][1:])
		
		elif "falls" in log:
			start = int(log[1][3:-1])
		
		elif "wakes" in log:
			end = int(log[1][3:-1])

			if current_guard not in sleep_data:
				sleep_data[current_guard] = {}

			for i in range(start, end):
				if i not in sleep_data[current_guard]:
					sleep_data[current_guard][i] = 1
				else:
					sleep_data[current_guard][i] += 1

	best_minute = None
	best_guard = None

	most = 0

	for guard in sleep_data:
		for minute in sleep_data[guard]:
			if sleep_data[guard][minute] > most:
				most = sleep_data[guard][minute]
				best_guard = guard
				best_minute = minute

	
	return best_guard * best_minute


def main():
	input_file = "day04-input.txt"
	print(solve(input_file))


if __name__ == "__main__":
	main()