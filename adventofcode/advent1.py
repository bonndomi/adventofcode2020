import itertools

import numpy

def find_2020(input_list, combination_nr):
    comb = itertools.combinations(input_list, combination_nr)
    for i in comb:
        if sum(i) != 2020:
            continue
        result = numpy.prod(i)
        return result


def main(user_data_file, combination_nr):
    input = load_input(user_data_file)
    result = find_2020(input, combination_nr)
    return result


def load_input(user_data_file):
    with open(user_data_file, "r") as input:
        for i in input:
            input_int = int(i)
            yield input_int
