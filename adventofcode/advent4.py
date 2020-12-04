import typing


def load_input(user_data_file):
    with open(user_data_file, "r") as fd:
        for line in fd:
            yield line.strip()


def read_passports(lines: typing.Iterable[str]) -> list:
    result = {}
    for line in lines:
        if line == "":
            yield result
            result = {}
            continue
        splitted = line.split(" ")
        for string in splitted:
            key, _, value = string.partition(":")
            result[key] = value


HACKED_KEYS = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}

def check_passport(passport: dict) -> bool:
    passport_set = set(passport.keys())
    return passport_set.issuperset(HACKED_KEYS)


def main1(input_file):
    lines = load_input(input_file)
    passports = read_passports(lines)
    count = 0
    for i, passport in enumerate(passports):
        if check_passport(passport):
            count += 1
        else:
            missing=set(passport).symmetric_difference(HACKED_KEYS)
            print(f"passport {i} is invalid, missing {missing}",)

    return count
