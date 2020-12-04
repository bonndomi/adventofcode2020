from collections import Counter


def load_input(user_data_file):
    with open(user_data_file, "r") as fd:
        for line in fd:
            yield line.strip()


def get_params(input):
    min, _, rest = input.partition('-')
    max, _, rest = rest.partition(' ')
    letter, _, pswd = rest.partition(': ')
    min = int(min)
    max = int(max)
    return min, max, letter, pswd


def check_old_validity(input: str) -> bool:
    min, max, letter, pswd = get_params(input)
    counts_letter = Counter(pswd)[letter]
    return min <= counts_letter <= max


def main1(input_file) -> int:
    lines = load_input(input_file)
    count = 0
    for line in lines:
        if check_old_validity(line):
            count += 1
    return count


def check_new_validity(input: str) -> bool:
    min, max, letter, pswd = get_params(input)
    first = pswd[min - 1] == letter
    second = pswd[max - 1] == letter
    return first != second

def main2(input_file) -> int:
    lines = load_input(input_file)
    count = 0
    for line in lines:
        if check_new_validity(line):
            count += 1
    return count
