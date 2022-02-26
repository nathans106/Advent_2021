def parse_ints(file):
    with open(file) as f:
        return [int(line) for line in f.readlines()]


def parse_strings(file):
    with open(file) as f:
        return [line.strip() for line in f.readlines()]


def make_matrix(lines):
    return [[int(num) for num in line.split(' ')] for line in lines]
