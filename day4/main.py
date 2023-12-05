from utils import get_input_lines

def main():
	puzzle = get_input_lines("puzzle.txt")
	# print(puzzle)
	res = 0
	for line in puzzle:
		win, mine = line.split(":")[1].split("|")
		win = [int(num) for num in win.split()]
		mine = [int(num) for num in mine.split()]
		value = 0
		for num in win:
			if num in mine:
				value = 2*value if value is not 0 else 1
		res += value

	print(res)
		# print(card)
	# print(games)








if __name__ == '__main__':
	main()
