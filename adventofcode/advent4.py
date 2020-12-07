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
        splitted = line.split()
        for string in splitted:
            key, _, value = string.partition(":")
            result[key] = value
    if result:
        yield result


HACKED_KEYS = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}


def check_fields_present(passport: dict) -> bool:
    passport_set = set(passport.keys())
    return passport_set.issuperset(HACKED_KEYS)


def main1(input_file: str) -> int:
    lines = load_input(input_file)
    passports = read_passports(lines)
    count = 0
    for i, passport in enumerate(passports):
        if check_fields_present(passport):
            count += 1
    return count


def validate_byr(element: str):
    if len(element) == 4 and element.isdecimal():
        int_element = int(element)
        return 1920 <= int_element <= 2002
    else:
        return False


def validate_iyr(element):
    try:
        int_element = int(element)
        return 2010 <= int_element <= 2020
    except ValueError:
        return False


def validate_eyr(element):
    try:
        int_element = int(element)
        return 2020 <= int_element <= 2030
    except ValueError:
        return False


def validate_hgt(element: str):
    try:
        if element.endswith("in"):
            number = int(element.removesuffix("in"))
            return 59 <= number <= 76
        elif element.endswith("cm"):
            number = int(element.removesuffix("cm"))
            return 150 <= number <= 193
    except ValueError:
        pass
    return False


def validate_hcl(element: str):
    if element.startswith("#") and len(element) == 7:
        color = element.removeprefix("#")
        try:
            int(color, 16)
            return True
        except ValueError:
            return False
    else:
        return False


def validate_ecl(element: str):
    return element in ("amb", "blu", "brn", "gry", "grn", "hzl", "oth")


def validate_pid(element: str):
    return element.isdecimal() and len(element) == 9


def validate_passport(passport: typing.Dict[str, str]):
    ecl = validate_ecl(passport["ecl"])
    pid = validate_pid(passport["pid"])
    hcl = validate_hcl(passport["hcl"])
    eyr = validate_eyr(passport["eyr"])
    hgt = validate_hgt(passport["hgt"])
    byr = validate_byr(passport["byr"])
    iyr = validate_iyr(passport["iyr"])

    return ecl and pid and hcl and eyr and hgt and byr and iyr


def main2(input_file:str) -> int:
    lines = load_input(input_file)
    passports = read_passports(lines)
    count = 0
    for i, passport in enumerate(passports):
        if check_fields_present(passport) and validate_passport(passport):
            count += 1
    return count
