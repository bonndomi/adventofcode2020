import typing
from collections import Counter


def load_input(user_data_file):
    with open(user_data_file, "r") as fd:
        for line in fd:
            yield line.strip()


def read_groups(lines: typing.Iterable[str]) -> typing.Iterable[list]:
    result = []
    for line in lines:
        if line == "":
            yield result
            result = []
            continue
        else:
            result.append(line)
    if result:
        yield result


def group_questions(group_entries: list[str]) -> dict[str, int]:
    """
    Receives the answers from the whole group, and returns, for each
    question, how many in the group answered yes
    """
    result = []
    for entry in group_entries:
        for answer in entry:
            result.append(answer)
    result_dict = Counter(result)
    return result_dict


def main1(input_file: str) -> int:
    group_entries = load_input(input_file)
    groups = read_groups(group_entries)
    count = 0
    for group in groups:
        unique_answers = group_questions(group)
        count += len(unique_answers)
    return count


def main2(input_file: str):
    group_entries = load_input(input_file)
    groups = read_groups(group_entries)
    count = 0
    for group in groups:
        answers = group_questions(group)
        for answer, times in answers.items():
            if times == len(group):
                count += 1
    return count
