import os.path

import pytest
from adventofcode import advent6


def test_advent6(user, user_data, record_testsuite_property):
    file = os.path.join(user_data, "6.txt")
    result1 = advent6.main1(file)
    record_testsuite_property(f"{user}-6-1", result1)
    result2 = advent6.main2(file)
    record_testsuite_property(f"{user}-6-2", result2)


@pytest.mark.parametrize(
    "input,expected",
    (
            pytest.param(["abc"], {"a": 1, "b": 1, "c": 1}, id="example1"),
            pytest.param(["a", "b", "c"], {"a": 1, "b": 1, "c": 1}, id="example2"),
            pytest.param(["ab", "ac"], {"a": 2, "b": 1, "c": 1}, id="example3"),
            pytest.param(["a", "a", "a", "a"], {"a": 4}, id="example4"),
            pytest.param(["b"], {"b": 1}, id="example5"),
    ),
)
def test_group_questions(input, expected):
    assert advent6.group_questions(input) == expected
