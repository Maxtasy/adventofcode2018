# https://adventofcode.com/2018/day/7

def part2(input_file):
	with open(input_file, "r") as f:
		lines = f.read().strip().split("\n")

	switch_ids = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

	switches = {k: [0,[]] for k in switch_ids}

	for line in lines:
		parts = line.split()
		switch = parts[7]
		dependency = parts[1]
		switches[switch][1].append(dependency)

	workers = {k: [None, None] for k in range(5)}

	# Get all available switches

	processed = ""

	process_times = {k: 60 + t for t, k in enumerate(switch_ids, start=1)}

	passed_time = 0

	while True:
		# Check workers for finished processes
		for worker in workers:
			# If worker is processing
			if workers[worker][0]:
				# Add 1 second of processing time
				workers[worker][1] += 1
				# If process time is reached
				if workers[worker][1] == process_times[workers[worker][0]]:
					# Free worker and set switch to true
					switches[workers[worker][0]][0] = 1
					workers[worker][0] = None
					workers[worker][1] = None


		# Update available switches
		availables = []

		for switch in switches:
			if switch not in processed:
				possible = True

				if switches[switch][1]:
					for dependency in switches[switch][1]:
						if switches[dependency][0] == 0:
							possible = False
							break

				if possible:
					availables.append(switch)


		# Start processes on idle workers
		for worker in workers:
			# If worker is not busy
			if workers[worker][0] == None:
				# If there are available switches 
				if availables:
					switch_to_process = min(availables)
					workers[worker][0] = switch_to_process
					workers[worker][1] = 0
					# Add the switch to our processed list
					processed += switch_to_process
					availables.remove(switch_to_process)

					#print(switch_to_process + " starts at " + str(passed_time) + " done at " + str(passed_time + process_times[switch_to_process]))


		# Check if no worker is busy
		busy = False

		for worker in workers:
			if workers[worker][0]:
				busy = True
				break 

		if not availables and not busy:
			break

		passed_time += 1

	return passed_time

def main():
	input_file = "day07-input.txt"
	print(part2(input_file))

if __name__ == "__main__":
	main()