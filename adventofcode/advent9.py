import collections
import itertools
import typing


def load_input(user_data_file):
    with open(user_data_file, "r") as fd:
        for line in fd:
            yield int(line)


def first_unmatching_number(
    numbers: typing.Iterator[int], tail_size: int
) -> typing.Optional[int]:
    tail = collections.deque(maxlen=tail_size)
    sums = {}
    for number in numbers:
        if len(tail) == tail_size:
            if number not in itertools.chain(*sums.values()):
                return number
            previous_number = tail.popleft()
            del sums[previous_number]
        for n in tail:
            sums[n].append(n + number)
        sums[number] = collections.deque(maxlen=tail_size)
        tail.append(number)
    return None


def main1(input_file, tail_size):
    numbers = load_input(input_file)
    number = first_unmatching_number(numbers, tail_size)
    return number


def find_combination_value(
    numbers: typing.Sequence[int], target: int
) -> typing.Optional[tuple[int, int]]:
    stack: list[typing.TypedDict("", {"min": int, "max": int, "sum": int})] = []
    for number in numbers:
        stack = [
            {
                "sum": number + s["sum"],
                "max": max(s["max"], number),
                "min": min(s["min"], number),
            }
            for s in stack
        ]
        stack.append({"sum": number, "max": number, "min": number})
        for s in stack:
            if target == s["sum"]:
                return s["min"], s["max"]
        stack = [s for s in stack if s["sum"] < target]


def main2(input_file, tail_size):
    numbers = list(load_input(input_file))
    target = first_unmatching_number(numbers, tail_size)
    mn, mx = find_combination_value(numbers, target)
    return mn + mx
