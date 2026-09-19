# https://adventofcode.com/2018/day/24

import re

LINE_RE = re.compile(
	r"(\d+) units each with (\d+) hit points(?: \(([^)]*)\))? "
	r"with an attack that does (\d+) (\w+) damage at initiative (\d+)"
)


class Group:
	def __init__(self, army, units, hp, modifiers, atk_damage, atk_type, initiative):
		self.army = army
		self.units = units
		self.hp = hp
		self.atk_damage = atk_damage
		self.atk_type = atk_type
		self.initiative = initiative

		self.weaknesses = set()
		self.immunities = set()
		if modifiers:
			for part in modifiers.split("; "):
				kind, types = part.split(" to ")
				types = set(t.strip() for t in types.split(","))
				if kind == "weak":
					self.weaknesses = types
				else:
					self.immunities = types

	@property
	def effective_power(self):
		return self.units * self.atk_damage

	@property
	def alive(self):
		return self.units > 0

	def damage_to(self, other):
		if self.atk_type in other.immunities:
			return 0
		multiplier = 2 if self.atk_type in other.weaknesses else 1
		return self.effective_power * multiplier


def parse(input_file):
	with open(input_file) as f:
		content = f.read()

	immune_block, infection_block = content.split("Infection:")
	immune_block = immune_block.replace("Immune System:", "").strip()
	infection_block = infection_block.strip()

	groups = []
	for line in immune_block.split("\n"):
		m = LINE_RE.match(line.strip())
		units, hp, modifiers, dmg, dmg_type, init = m.groups()
		groups.append(Group("immune", int(units), int(hp), modifiers, int(dmg), dmg_type, int(init)))

	for line in infection_block.split("\n"):
		m = LINE_RE.match(line.strip())
		units, hp, modifiers, dmg, dmg_type, init = m.groups()
		groups.append(Group("infection", int(units), int(hp), modifiers, int(dmg), dmg_type, int(init)))

	return groups


def fight(groups):
	groups = [g for g in groups if g.alive]

	while True:
		armies = set(g.army for g in groups)
		if len(armies) < 2:
			break

		# Target selection.
		groups.sort(key=lambda g: (-g.effective_power, -g.initiative))
		targets = {}
		taken = set()
		for g in groups:
			enemies = [e for e in groups if e.army != g.army and id(e) not in taken]
			if not enemies:
				continue
			best = max(enemies, key=lambda e: (g.damage_to(e), e.effective_power, e.initiative))
			if g.damage_to(best) > 0:
				targets[id(g)] = best
				taken.add(id(best))

		# Attack phase, in initiative order.
		groups.sort(key=lambda g: -g.initiative)
		any_died = False
		for g in groups:
			if not g.alive:
				continue
			target = targets.get(id(g))
			if target is None or not target.alive:
				continue
			damage = g.damage_to(target)
			killed = min(target.units, damage // target.hp)
			if killed > 0:
				any_died = True
			target.units -= killed

		groups = [g for g in groups if g.alive]

		if not any_died:
			# Stalemate: no progress will ever be made again.
			return None, groups

	winner = groups[0].army if groups else None
	return winner, groups


def part1(input_file):
	groups = parse(input_file)
	winner, survivors = fight(groups)
	return sum(g.units for g in survivors)


def main():
	input_file = "day24-input.txt"
	print(part1(input_file))


if __name__ == "__main__":
	main()
