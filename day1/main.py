from functools import reduce
def main():
	with open('puzzle.txt') as f:
		lines = f.readlines()
	part_one(lines)
	part_two(lines)

def part_one(lines):
	puzzle = [line.strip() for line in lines]
	puzzle2 = [get_digits(s) for s in puzzle]
	puzzle2 = list(map(int, puzzle2))
	answer = reduce(lambda x, y: x + y, puzzle2)
	print(f'part one is {answer}')

def part_two(lines):
	puzzle = [line.strip() for line in lines]
	puzzle2 = [parsed(s) for s in puzzle]
	puzzle2 = [get_digits(s) for s in puzzle2]
	# print(puzzle2)
	puzzle2 = list(map(int, puzzle2))
	answer = reduce(lambda x, y: x + y, puzzle2)
	print(f'part two is {answer}')

def parsed(s):
	digit_dic = {
		'one': 'o1e',
		'two': 't2o',
		'three': 'th3ee',
		'four': 'f4r',
		'five': 'f5e',
		'six': 's6x',
		'seven': 's7n',
		'eight': 'e8t',
		'nine': 'n9e'
		}
	for k,v in digit_dic.items():
		s = s.replace(k, v)
	return s

def get_digits(s):
	first_digit = None
	for i, c in enumerate(s):
		if c.isdigit():
			first_digit = c
			break
	last_digit = None
	for i, c in enumerate(s[::-1]):
		if c.isdigit():
			last_digit = c
			break
	return first_digit + last_digit

if __name__ == '__main__':
	main()
