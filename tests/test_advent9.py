import itertools
import os

import pytest

from adventofcode import advent9


def test_advent9(user, user_data, record_testsuite_property):
    file = os.path.join(user_data, "9.txt")
    tail_size = 25
    if user == "reference":
        tail_size = 5
    result = advent9.main1(file, tail_size)
    record_testsuite_property(f"{user}-9-1", result)
    result = advent9.main2(file, tail_size)
    record_testsuite_property(f"{user}-9-2", result)


@pytest.mark.parametrize(
    "numbers,tail,expected",
    (
        pytest.param(
            list(itertools.chain(range(1, 26), [26])),
            25,
            None,
            id="example-1",
        ),
        pytest.param(
            list(itertools.chain(range(1, 26), [49])), 25, None, id="example-2"
        ),
        pytest.param(
            list(itertools.chain(range(1, 26), [100])), 25, 100, id="example-3"
        ),
        pytest.param(list(itertools.chain(range(1, 26), [50])), 25, 50, id="example-4"),
        pytest.param(
            list(itertools.chain([20], range(1, 20), range(21, 26), [45, 26])),
            25,
            None,
            id="example-5",
        ),
        pytest.param(
            list(itertools.chain([20], range(1, 20), range(21, 26), [45, 65])),
            25,
            65,
            id="example-6",
        ),
        pytest.param(
            list(itertools.chain([20], range(1, 20), range(21, 26), [45, 64])),
            25,
            None,
            id="example-7-1",
        ),
        pytest.param(
            list(itertools.chain([20], range(1, 20), range(21, 26), [45, 66])),
            25,
            None,
            id="example-7-2",
        ),
        pytest.param(
            [
                35,
                20,
                15,
                25,
                47,
                40,
                62,
                55,
                65,
                95,
                102,
                117,
                150,
                182,
                127,
                219,
                299,
                277,
                309,
                576,
            ],
            5,
            127,
            id="example-8",
        ),
    ),
)
def test_first_unmatching_number(numbers, tail, expected):
    assert advent9.first_unmatching_number(numbers, tail) == expected


@pytest.mark.parametrize(
    "numbers,target,expected",
    (
        pytest.param(
            [
                35,
                20,
                15,
                25,
                47,
                40,
                62,
                55,
                65,
                95,
                102,
                117,
                150,
                182,
                127,
                219,
                299,
                277,
                309,
                576,
            ],
            127,
            (15, 47),
            id="example-9",
        ),
    ),
)
def test_find_combination_value(numbers, target, expected):
    assert advent9.find_combination_value(numbers, target) == expected
