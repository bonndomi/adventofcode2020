import pytest
import os.path

from adventofcode import advent4

def test_advent4(user_data, user, record_testsuite_property):
    file = os.path.join(user_data, '4.txt')
    result = advent4.main1(file)
    record_testsuite_property(f'{user}-4-1', result)
    # result = advent2.main2(file)
    # record_testsuite_property(f'{user}-4-2', result)

def test_read_passports():
    input = ['ecl:gry pid:860033327 eyr:2020 hcl:#fffffd', 'byr:1937 iyr:2017 cid:147 hgt:183cm', '',
             'iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884',
             'hcl:#cfa07d byr:1929', '', 'hcl:#ae17e1 iyr:2013', 'eyr:2024', 'ecl:brn pid:760753108 byr:1931',
             'hgt:179cm', '', 'hcl:#cfa07d eyr:2025 pid:166559648', 'iyr:2011 ecl:brn hgt:59in', '']

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
        ({'byr': '1937',
          'cid': '147',
          'ecl': 'gry',
          'eyr': '2020',
          'hcl': '#fffffd',
          'hgt': '183cm',
          'iyr': '2017',
          'pid': '860033327'}, True),
        ({'byr': '1929',
          'cid': '350',
          'ecl': 'amb',
          'eyr': '2023',
          'hcl': '#cfa07d',
          'iyr': '2013',
          'pid': '028048884'}, False),
        ({'byr': '1931',
          'ecl': 'brn',
          'eyr': '2024',
          'hcl': '#ae17e1',
          'hgt': '179cm',
          'iyr': '2013',
          'pid': '760753108'}, True),
        ({'ecl': 'brn',
          'eyr': '2025',
          'hcl': '#cfa07d',
          'hgt': '59in',
          'iyr': '2011',
          'pid': '166559648'}, False)
))
def test_check_passport(input, expected):
    assert advent4.check_passport(input) == expected
