import os.path
import pytest
from adventofcode import advent5


def test_advent5(user_data, user, record_testsuite_property):
    file = os.path.join(user_data, '5.txt')
    result = advent5.main1(file)
    record_testsuite_property(f'{user}-5-1', result)
    result = advent5.main2(file)
    record_testsuite_property(f'{user}-5-2', result)


@pytest.mark.parametrize('input,expected', (
        ("FBFBBFFRLR", 357),
        ("BFFFBBFRRR", 567),
        ("FFFBBBFRRR", 119),
        ("BBFFBBFRLL", 820),
))
def test_get_seat(input, expected):
    assert advent5.get_seat(input) == expected
