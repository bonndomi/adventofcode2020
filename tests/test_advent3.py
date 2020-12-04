import os.path

import pytest

from adventofcode import advent3


def test_advent3(user_data, user, record_testsuite_property):
    input_file = os.path.join(user_data, "3.txt")
    result = advent3.main1(input_file)
    record_testsuite_property(f'{user}-3-1', result)
    result = advent3.main2(input_file)
    record_testsuite_property(f'{user}-3-2', result)


def test_read_1_3_lines():
    input = [
                "0111111111",
                "1110111111",
                "1111110111",
                "1111111110",
                "1101111111",
                "1111101111",
                "1111111101",
                "1011111111",
                "1111011111",
                "1111111011",
                "0111111111",
            ]
    result = advent3.read_1_3_lines(iter(input))
    for i, r in enumerate(result):
        assert r == "0", f'Line {i} returned {r} instead of "0"'


@pytest.mark.parametrize('input,pattern', (
        (
                [
                    "0111111111",
                    "1011111111",
                    "1101111111",
                    "1110111111",
                    "1111011111",
                    "1111101111",
                    "1111110111",
                    "1111111011",
                    "1111111101",
                    "1111111110",
                    "0111111111",
                ],
                (1, 1),
        ),
        (
                [
                    "0111111111",
                    "1110111111",
                    "1111110111",
                    "1111111110",
                    "1101111111",
                    "1111101111",
                    "1111111101",
                    "1011111111",
                    "1111011111",
                    "1111111011",
                    "0111111111",
                ],
                (1, 3),
        ),
        (
                [
                    "0111111111",
                    "1111101111",
                    "0111111111",
                    "1111101111",
                    "0111111111",
                    "1111101111",
                    "0111111111",
                    "1111101111",
                    "0111111111",
                    "1111101111",
                ],
                (1, 5),
        ),
        (
                [
                    "0111111111",
                    "1111111011",
                    "1111011111",
                    "1011111111",
                    "1111111101",
                    "1111101111",
                    "1101111111",
                    "1111111110",
                    "1111110111",
                    "1110111111",
                    "0111111111",
                ],
                (1, 7),
        ),
        (
                [
                    "0111111111",
                    "1111111111",
                    "1011111111",
                    "1111111111",
                    "1101111111",
                    "1111111111",
                    "1110111111",
                    "1111111111",
                    "1111011111",
                    "1111111111",
                    "1111101111",
                ],
                (2, 1),
        ),
))
def test_read_pattern_lines(input, pattern):
    result = advent3.read_pattern_lines(iter(input), pattern)
    for i, r in enumerate(result):
        assert r == "0", f'Line {i} returned {r} instead of "0"'
