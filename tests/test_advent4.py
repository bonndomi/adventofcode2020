import os.path

import pytest
from adventofcode import advent4


def test_advent4(user_data, user, record_testsuite_property):
    file = os.path.join(user_data, '4.txt')
    result = advent4.main1(file)
    record_testsuite_property(f'{user}-4-1', result)
    result = advent4.main2(file)
    record_testsuite_property(f'{user}-4-2', result)


def test_read_passports():
    input = ['ecl:gry pid:860033327 eyr:2020 hcl:#fffffd', 'byr:1937 iyr:2017 cid:147 hgt:183cm', '',
             'iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884',
             'hcl:#cfa07d byr:1929', '', 'hcl:#ae17e1 iyr:2013', 'eyr:2024', 'ecl:brn pid:760753108 byr:1931',
             'hgt:179cm', '', 'hcl:#cfa07d eyr:2025 pid:166559648', 'iyr:2011 ecl:brn hgt:59in']

    output = [{'byr': '1937',
               'cid': '147',
               'ecl': 'gry',
               'eyr': '2020',
               'hcl': '#fffffd',
               'hgt': '183cm',
               'iyr': '2017',
               'pid': '860033327'},
              {'byr': '1929',
               'cid': '350',
               'ecl': 'amb',
               'eyr': '2023',
               'hcl': '#cfa07d',
               'iyr': '2013',
               'pid': '028048884'},
              {'byr': '1931',
               'ecl': 'brn',
               'eyr': '2024',
               'hcl': '#ae17e1',
               'hgt': '179cm',
               'iyr': '2013',
               'pid': '760753108'},
              {'ecl': 'brn',
               'eyr': '2025',
               'hcl': '#cfa07d',
               'hgt': '59in',
               'iyr': '2011',
               'pid': '166559648'}]

    assert list(advent4.read_passports(input)) == output


@pytest.mark.parametrize("input, expected", (
        pytest.param({'byr': '1937',
                      'cid': '147',
                      'ecl': 'gry',
                      'eyr': '2020',
                      'hcl': '#fffffd',
                      'hgt': '183cm',
                      'iyr': '2017',
                      'pid': '860033327'}, True, id="original-passport"),
        pytest.param({'byr': '1929',
                      'cid': '350',
                      'ecl': 'amb',
                      'eyr': '2023',
                      'hcl': '#cfa07d',
                      'iyr': '2013',
                      'pid': '028048884'}, False, id="missing-required"),
        pytest.param({'byr': '1931',
                      'ecl': 'brn',
                      'eyr': '2024',
                      'hcl': '#ae17e1',
                      'hgt': '179cm',
                      'iyr': '2013',
                      'pid': '760753108'}, True, id="northern-pole-id-missing-cid"),
        pytest.param({'ecl': 'brn',
                      'eyr': '2025',
                      'hcl': '#cfa07d',
                      'hgt': '59in',
                      'iyr': '2011',
                      'pid': '166559648'}, False, id="missing-cid-and-byr")
))
def test_check_field_present(input, expected):
    assert advent4.check_fields_present(input) == expected


@pytest.mark.parametrize('input,expected', (
        pytest.param("2002", True, id="example-1"),
        pytest.param("2003", False, id="example-2"),
        pytest.param("123", False, id="three-digits"),
        pytest.param("02000", False, id="five-digits"),
        pytest.param("0123", False, id="lower"),
        pytest.param("1919", False, id="too-small"),
        pytest.param("1920", True, id="correct-range-down"),
        pytest.param("2002", True, id="correct-range-up"),
        pytest.param("2003", False, id="too-big"),
))
def test_validate_byr(input, expected):
    assert advent4.validate_byr(input) == expected


@pytest.mark.parametrize('input, expected', (
        pytest.param("123", False, id="three-digits"),
        pytest.param("02000", False, id="five-digits"),
        pytest.param("0123", False, id="lower"),
        pytest.param("2009", False, id="too-small"),
        pytest.param("2010", True, id="correct-range-down"),
        pytest.param("2020", True, id="correct-range-up"),
        pytest.param("2021", False, id="too-big"),
))
def test_validate_iyr(input, expected):
    assert advent4.validate_iyr(input) == expected


@pytest.mark.parametrize('input,expected', (
        pytest.param("123", False, id="three-digits"),
        pytest.param("02000", False, id="five-digits"),
        pytest.param("0123", False, id="lower"),
        pytest.param("2019", False, id="too-small"),
        pytest.param("2020", True, id="correct-range-down"),
        pytest.param("2030", True, id="correct-range-up"),
        pytest.param("2031", False, id="too-big"),
))
def test_validate_eyr(input, expected):
    assert advent4.validate_eyr(input) == expected


@pytest.mark.parametrize('input,expected', (
        pytest.param("60in", True, id="example-1"),
        pytest.param("190cm", True, id="example-2"),
        pytest.param("190in", False, id="example-3"),
        pytest.param("190", False, id="example-4"),
        pytest.param("aacm", False, id="letters-followed-by-cm"),
        pytest.param("aain", False, id="letters-followed-by-in"),
        pytest.param("12", False, id="numbers-only"),
        pytest.param("aaaa", False, id="letters-only"),
        pytest.param("149cm", False, id="cm-too-small"),
        pytest.param("150cm", True, id="cm-correct-range-down"),
        pytest.param("193cm", True, id="cm-correct-range-up"),
        pytest.param("194cm", False, id="cm-too-big"),
        pytest.param("58in", False, id="in-too-small"),
        pytest.param("59in", True, id="in-correct-range-down"),
        pytest.param("76in", True, id="in-correct-range-up"),
        pytest.param("77in", False, id="in-too-big"),
))
def test_validate_hgt(input, expected):
    assert advent4.validate_hgt(input) == expected


@pytest.mark.parametrize('input,expected', (
        pytest.param("#123abc", True, id="example-1"),
        pytest.param("#123abz", False, id="example-2"),
        pytest.param("123abc", False, id="example-3"),
        pytest.param("$123456", False, id="dollar-number"),
        pytest.param("#1234567", False, id="hash-seven-number"),
        pytest.param("#01234567", False, id="hash-zero-seven-number"),
        pytest.param("#123456", True, id="hash-number"),
        pytest.param("#023456", True, id="hash-zero-number"),
        pytest.param("#abcdef", True, id="hash-hex"),
        pytest.param("#123def", True, id="hash-number-hex"),
))
def test_validate_hcl(input, expected):
    assert advent4.validate_hcl(input) == expected


@pytest.mark.parametrize('input,expected', (
        pytest.param("brn", True, id="example-1"),
        pytest.param("wat", False, id="example-2"),
        pytest.param("aaa", False, id="invalid"),
        pytest.param("amb", True, id="amber"),
        pytest.param("blu", True, id="blue"),
        pytest.param("brn", True, id="brown"),
        pytest.param("gry", True, id="grey"),
        pytest.param("grn", True, id="green"),
        pytest.param("hzl", True, id="hzl"),
        pytest.param("oth", True, id="oth"),
))
def test_validate_ecl(input, expected):
    assert advent4.validate_ecl(input) == expected


@pytest.mark.parametrize('input,expected', (
        pytest.param("000000001", True, id="example-1"),
        pytest.param("0123456789", False, id="example-2"),
        pytest.param("1123456789", False, id="ten-digits"),
        pytest.param("0123456789", False, id="ten-digits-leading-zero"),
        pytest.param("123456789", True, id="nine-digits"),
        pytest.param("023456789", True, id="nine-digits-leading-zero"),
))
def test_validate_pid(input, expected):
    assert advent4.validate_pid(input) == expected

