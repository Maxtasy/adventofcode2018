# https://adventofcode.com/2018/day/9

def part1(n_players, n_marbles):
	marbles = list(range(n_marbles + 1))
	circle = []
	scores = [0] * n_players
	active_index = 0
	current_player = 0

	# While there are still marbles
	while marbles:
		# Set current player
		current_player = (current_player + 1) % n_players
		# Set current marble to lowest of the remaining marbles
		current_marble = marbles[0]

		if current_marble == 0:
			circle.append(0)

		# If marble is a multiple of 23
		elif current_marble % 23 == 0:
			active_index = (active_index - 7) % len(circle)
			marble_to_remove = circle[active_index]
			scores[current_player] += current_marble + marble_to_remove
			del circle[active_index]

		else:
			active_index = (active_index + 2) % len(circle)
			# Split list at index
			before, after = circle[:active_index], circle[active_index:]
			circle = before + [current_marble] + after
		
		# Remove the played marble from remaining marbles
		del marbles[0]

	return max(scores)

def main():
	parts = open("day09-input.txt").read().split()
	n_players = int(parts[0])
	n_marbles = int(parts[6])
	print(part1(n_players, n_marbles))

if __name__ == "__main__":
	main()