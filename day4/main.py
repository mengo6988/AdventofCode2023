from utils import get_input_lines

def main():
	puzzle = get_input_lines("puzzle.txt")
	# print(puzzle)
	res = 0
	count = [1] * len(puzzle)
	for line in puzzle:
		win, mine = line.split(":")[1].split("|")
		win = [int(num) for num in win.split()]
		mine = [int(num) for num in mine.split()]
		value = 0
		for num in win:
			if num in mine:
				value = 2*value if value != 0 else 1
		res += value
	for i, line in enumerate(puzzle):
		x,y = map(str.split, line.split('|'))
		n = len(set(x) & set(y))
		for j in range(i + 1, min(i+1+n,len(puzzle))):
			count[j] += count[i]
	print(sum(count))
	print(res)
		# print(card)
	# print(games)








if __name__ == '__main__':
	main()
