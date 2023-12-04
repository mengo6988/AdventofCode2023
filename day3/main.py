from utils import get_input_lines
import re
from functools import reduce

def main():
	data = get_input_lines("puzzle.txt")
	print(part_one(data))
	print(part_two(data))

def part_one(data):
	pattern = re.compile(r'[^\w\s.]')
	res = 0
	for y, line in enumerate(data):
		for x, char in enumerate(line):
			if re.match(pattern, char):
				res += check_surrounding(x, y, data)
	return res

def part_two(data):
	pattern = re.compile(r'\*')
	res = 0
	for y, line in enumerate(data):
		for x, char in enumerate(line):
			if re.match(pattern, char):
				res += check_surrounding(x, y, data, part2=True)
	return res

def check_surrounding(x, y, data, part2 = False):
	res = []
	for j in range(y - 1, y + 2):
		if j >= 0 and j < len(data):
			flag = False
			for i in range(x - 1, x + 2):
				if i >= 0 and i < len(data[j]):
					if data[j][i].isdigit() and not flag:
						res.append(int(get_nums(i, data[j])))
						flag = True
					if not data[j][i].isdigit():
						flag = False
	if part2 :
		if len(res) == 2:
			return reduce(lambda x,y: x * y, res)
		else:
			return 0
	else:
		return sum(res)


def get_nums(x, line):
	num = [line[x]]
	for i in range(1, 3):
		if i >= 0 and line[x - i].isdigit():
			num.insert(0, line[x - i])
		else:
			break
	for i in range(1, 3):
		if i < len(line) and line[x + i].isdigit():
			num.append(line[x + i])
		else:
			break
	num = ''.join(num)
	return num

if __name__ == "__main__":
	main()
