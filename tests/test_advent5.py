import pytest
from adventofcode import advent5


def test_advent5(user_data, user, record_testsuite_property):
    file = os.path.join(user_data, '5.txt')
    result = advent5.main1(file)
    record_testsuite_property(f'{user}-5-1', result)
    result = advent5.main2(file)
    record_testsuite_property(f'{user}-5-2', result)
