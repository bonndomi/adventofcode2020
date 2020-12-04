import os.path

import pytest

from adventofcode import advent1


def test_advent1(user, user_data, record_testsuite_property):
    file = os.path.join(user_data, '1.txt')
    result1 = advent1.main(file, 2)
    result2 = advent1.main(file, 3)
    record_testsuite_property(f'{user}-1-1', result1)
    record_testsuite_property(f'{user}-1-2', result2)
