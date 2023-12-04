from utils import get_input_lines
from functools import reduce

COLOURS = {
	'red': 12,
	'green': 13,
	'blue': 14
}

def main():
	puzzle = get_input_lines("puzzle.txt")
	res = 0
	for i, game in enumerate(puzzle):
		if check_game(game) == True:
			res += (i + 1)
	print(f'part one = {res}')
	res2 = 0
	for i, game in enumerate(puzzle):
		res2 += get_sum_games(game)
	print(f'part two = {res2}')

def check_game(puzzle):
	rounds = puzzle.split(":")[1].split(";")
	for round in rounds:
		colors = round.split(",")
		for color in colors:
			n, c = color.strip().split(" ")
			if int(n) > COLOURS[c]:
				return False
	return True

def get_sum_games(puzzle):
	colors_min = {
		'red': 0,
		'green': 0,
		'blue': 0
	}
	rounds = puzzle.split(":")[1].split(";")
	for round in rounds:
		colors = round.split(",")
		for color in colors:
			n, c = color.strip().split(" ")
			if int(n) > colors_min[c]:
				colors_min[c] = int(n)
	return reduce(lambda x, y: x * y, colors_min.values())


if __name__ == '__main__':
	main()
