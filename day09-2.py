# https://adventofcode.com/2018/day/9

from collections import deque

def part2(n_players, n_marbles):
	n_players = 476
	n_marbles = 7143100
	circle = deque([0])
	scores = [0] * n_players
	current_player = 0

	# For each marble in the remaining marbles
	for current_marble in range(1, n_marbles + 1):
		# Set current player
		current_player = (current_player + 1) % n_players

		# If marble is a multiple of 23
		if current_marble % 23 == 0:
			circle.rotate(7)
			scores[current_player] += current_marble + circle.pop()
			circle.rotate(-1)

		else:
			circle.rotate(-1)
			circle.append(current_marble)

	return max(scores)

def main():
	parts = open("day09-input.txt").read().split()
	n_players = int(parts[0])
	n_marbles = int(parts[6])
	print(part2(n_players, n_marbles))

if __name__ == "__main__":
	main()