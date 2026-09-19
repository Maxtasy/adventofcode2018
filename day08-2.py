# https://adventofcode.com/2018/day/8


def parse(data):
	children, metas = data[:2]
	data = data[2:]
	scores = []
	totals = 0

	for i in range(children):
		total, score, data = parse(data)
		totals += total
		scores.append(score)

	totals += sum(data[:metas])

	if children == 0:
		return totals, sum(data[:metas]), data[metas:]
	else:
		return (
			totals,
			sum(scores[k - 1] for k in data[:metas] if k > 0 and k <= len(scores)),
			data[metas:],
		)


def part2(input_file):
	with open(input_file, "r") as f:
		data = [int(x) for x in f.read().split()]

	_, value, _ = parse(data)
	return value


def main():
	input_file = "day08-input.txt"
	print(part2(input_file))


if __name__ == "__main__":
	main()
