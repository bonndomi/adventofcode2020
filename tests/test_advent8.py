import os

import pytest

from adventofcode import advent8


def test_advent8(user, user_data, record_testsuite_property):
    file = os.path.join(user_data, "7.txt")
    result = advent8.main1(file)
    record_testsuite_property(f"{user}-7-1", result)
    result = advent8.main2(file)
    record_testsuite_property(f"{user}-7-2", result)


@pytest.mark.parametrize(
    "input,expected",
    (
            pytest.param(("nop +0", "acc +1", "jmp +4", "acc +3", "jmp -3", "acc -99", "acc +1", "jmp -4", "acc +6"),
            {"position": 1, "accumulator": 5})))

def test_main1(input, expected):
    assert advent8.main1(input) == expected
