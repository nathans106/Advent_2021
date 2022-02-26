def parse_ints(file):
    with open(file) as f:
        return [int(line) for line in f.readlines()]

