import typing


def read_bag_rule(line) -> tuple[str, dict[str, int]]:
    """Read a line description of the bag possible contents and return
    a data structure of the parsed line

    For example:
    light red bags contain 1 bright white bag, 2 muted yellow bags.

    Would return:
    ('light red', {"bright white": 1, "mutted yellow", 2})
    """
    pass


def upstream_dependencies(
    bag_descriptions: typing.Iterable[tuple[str, dict[str, int]]]
) -> dict[str, dict[str, int]]:
    """
    With all the bag descriptions, creates a reversed tree in which
    the keys are the childs, and the values are dictionaries where
    parents are the keys and values are the amount of items they have.

    For example
    [
        {'light red', {"bright white": 1, "mutted yellow": 2}},
        {'bright white', {"mutted yellow": 1}},
    ]

    Would return:
    {
        'bright white': { 'light red': 1 },
        'mutted yellow': { 'light red': 2, 'bright white': 1 }
    }
    """
    pass


def main1(input_file) -> int:
    pass


def main2(input_file):
    pass
