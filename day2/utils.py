def get_input_lines(filename):
	with open(filename) as f:
		lines = f.readlines()
	puzzle = [line.strip() for line in lines]
	return puzzle
