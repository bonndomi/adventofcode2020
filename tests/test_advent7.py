import os

import pytest

from adventofcode import advent7


def test_advent7(user, user_data, record_testsuite_property):
    file = os.path.join(user_data, "7.txt")
    result = advent7.main1(file)
    record_testsuite_property(f"{user}-7-1", result)
    result = advent7.main2(file)
    record_testsuite_property(f"{user}-7-2", result)


@pytest.mark.parametrize(
    "input,expected",
    (
            pytest.param(
                "light red bags contain 1 bright white bag, 2 muted yellow bags.",
                {"light red": {"bright white": 1, "muted yellow": 2}},
                id="example-1",
            ),
            pytest.param(
                "dark orange bags contain 3 bright white bags, 4 muted yellow bags.",
                {"dark orange": {"bright white": 3, "muted yellow": 4}},
                id="example-2",
            ),
            pytest.param(
                "bright white bags contain 1 shiny gold bag.",
                {"bright white": {"shiny gold": 1}},
                id="example-3",
            ),
            pytest.param(
                "muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.",
                {"muted yellow": {"shiny gold": 2, "faded blue": 9}},
                id="example-4",
            ),
            pytest.param(
                "shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.",
                {"shiny gold": {"dark olive": 1, "vibrant plum": 2}},
                id="example-5",
            ),
            pytest.param(
                "dark olive bags contain 3 faded blue bags, 4 dotted black bags.",
                {"dark olive": {"faded blue": 3, "dotted black": 4}},
                id="example-6",
            ),
            pytest.param(
                "vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.",
                {"vibrant plum": {"faded blue": 5, "dotted black": 6}},
                id="example-7",
            ),
            pytest.param(
                "faded blue bags contain no other bags.", {"faded blue": {}}, id="example-8"
            ),
            pytest.param(
                "dotted black bags contain no other bags.",
                {"dotted black": {}},
                id="example-9",
            ),
    ),
)
def test_read_bag_rule(input, expected):
    assert advent7.read_bag_rule(input) == expected


@pytest.mark.parametrize(
    "input,expected",
    (
            pytest.param(
                {
                    "light red": {"bright white": 1, "muted yellow": 2},
                    "bright white": {"muted yellow": 1},
                },
                {
                    "bright white": {"light red": 1},
                    "muted yellow": {"light red": 2, "bright white": 1},
                },
                id="two-upstream-dependencies",
            ),
    )
)
def test_upstream_dependencies(input, expected):
    assert advent7.upstream_dependencies(input) == expected
