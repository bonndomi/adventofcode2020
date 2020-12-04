import typing


def load_input(user_data_file):
    with open(user_data_file, "r") as fd:
        for line in fd:
            yield line.strip()


def read_1_3_lines(lines: typing.Iterator[str]) -> typing.Iterator[str]:
    position = 0
    for l in lines:
        yield l[position % len(l)]
        position += 3


def main1(input_file):
    lines = load_input(input_file)
    results = read_1_3_lines(lines)
    count = 0
    for char in results:
        if char == "#":
            count += 1
    return count


def read_pattern_lines(lines: typing.Iterator[str], pattern: tuple[int, int]) -> typing.Iterator[str]:
    y, x = pattern
    x_position = 0

    for i, l in enumerate(lines):
        if i % y != 0:
            continue
        yield l[x_position % len(l)]
        x_position += x

def main2(input_file):
    patterns = [(1, 1), (1, 3), (1, 5), (1, 7), (2, 1)]

    result = 1
    for pattern in patterns:
        count = 0
        lines = load_input(input_file)
        results = read_pattern_lines(lines, pattern)
        for char in results:
            if char == "#":
                count += 1
        result *= count
    return result
