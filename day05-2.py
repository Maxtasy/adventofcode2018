# https://adventofcode.com/2018/day/5

def react(input_file):
	with open(input_file, "r") as f:
		s = f.read().strip()

	#s = "wNnJZzjXxlLrWwbBaARdaADWfmMZzFDdKCcQTCaActfEeFqkKkpxXdPpDPEejbBCcuqQUFfQqJMmNnLlJhHLmMvVRrCcRrFRrjyYJfyQqYYLlyJjljjNqQdOzZoDgGtTJjWwnBUubQYyVvjJqUpPe"

	alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
	units = "abcdefghijklmnopqrstuvwxyz"

	results = []

	for unit in units:
		s_test = s[:]

		s_test = s_test.replace(unit, "").replace(unit.upper(), "")

		index = 0
		found = True

		while found:
			print(len(s_test), unit)
			found = False
			for i in range(index, len(s_test) - 1):
				if s_test[i] == alphabet[(alphabet.index(s_test[i + 1]) + 26) % 52]:
					found = True
					s_test = s_test[:i] + s_test[i + 2:]
					if index != 0:
						index = i - 1
					break

		results.append(len(s_test))
	
	return min(results)


def main():
	input_file = "day05-input.txt"
	print(react(input_file))


if __name__ == "__main__":
	main()