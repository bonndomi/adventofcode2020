import os

import pytest
from adventofcode import advent2


def test_advent2(user_data, user, record_testsuite_property):
    file = os.path.join(user_data, '2.txt')
    result = advent2.main1(file)
    record_testsuite_property(f'{user}-2-1', result)
    result = advent2.main2(file)
    record_testsuite_property(f'{user}-2-2', result)


@pytest.mark.parametrize('input,expected', (
        ('1-3 a: abcde', True),
        ('1-3 b: cdefg', False),
        ('2-9 c: ccccccccc', True),
))
def test_check_old_validity(input, expected):
    assert advent2.check_old_validity(input) is expected


@pytest.mark.parametrize('input,expected', (
        ('1-3 a: abcde', (1,3,'a','abcde')),
        ('1-3 b: cdefg', (1,3,'b', 'cdefg')),
        ('2-9 c: ccccccccc', (2,9,'c','ccccccccc')),
))
def test_get_params(input, expected):
    assert advent2.get_params(input) == expected

@pytest.mark.parametrize('input,expected', (
        ('1-3 a: abcde', True),
        ('1-3 b: cdefg', False),
        ('2-9 c: ccccccccc', False),
))
def test_check_new_validity(input, expected):
    assert advent2.check_new_validity(input) is expected
