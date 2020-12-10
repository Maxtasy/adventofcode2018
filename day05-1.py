# https://adventofcode.com/2018/day/5

def react(input_file):
	with open(input_file, "r") as f:
		s = f.read().strip()

	#s = "wNnJZzjXxlLrWwbBaARdaADWfmMZzFDdKCcQTCaActfEeFqkKkpxXdPpDPEejbBCcuqQUFfQqJMmNnLlJhHLmMvVRrCcRrFRrjyYJfyQqYYLlyJjljjNqQdOzZoDgGtTJjWwnBUubQYyVvjJqUpPe"

	alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

	index = 0

	found = True

	while found:
		#print(len(s))
		found = False
		for i in range(index, len(s) - 1):
			if s[i] == alphabet[(alphabet.index(s[i + 1]) + 26) % 52]:
				found = True
				s = s[:i] + s[i + 2:]
				if index != 0:
					index = i - 1
				break
	
	return len(s)


def main():
	input_file = "day05-input.txt"
	print(react(input_file))


if __name__ == "__main__":
	main()