import collections

def load_input(user_data_file):
    with open(user_data_file, "r") as fd:
        for line in fd:
            yield line.strip()


def read_bag_rule(line) -> dict[str, dict[str, int]]:
    """Read a line description of the bag possible contents and return
    a data structure of the parsed line

    For example:
    light red bags contain 1 bright white bag, 2 muted yellow bags.

    Would return:
    {'light red': {"bright white": 1, "muted yellow":, 2}}
    """
    outer_bag, _, inner_bags = line.partition(" bags contain ")
    inner_bags_split = inner_bags.split(", ")
    result = {}
    if inner_bags_split[0] != "no other bags.":
        for inner_bag in inner_bags_split:
            nr_bags, _, rest = inner_bag.partition(" ")
            bag_color, _, _ = rest.rpartition(" ")
            result[bag_color] = int(nr_bags)
    result_tuple = {outer_bag: result}
    return result_tuple


def upstream_dependencies(
        bag_descriptions: dict[str, dict[str, int]]
) -> dict[str, dict[str, int]]:
    """
    With all the bag descriptions, creates a reversed tree in which
    the keys are the children, and the values are dictionaries where
    parents are the keys and values are the amount of items they have.

    For example
    {
        'light red': {"bright white": 1, "muted yellow": 2},
        'bright white': {"muted yellow": 1},
    }

    Would return:
    {
        'bright white': { 'light red': 1 },
        'muted yellow': { 'light red': 2, 'bright white': 1 }
    }
    """
    result = collections.defaultdict(dict)
    for parent_bag, children_bags in bag_descriptions.items():
        for child_bag, value in children_bags.items():
            result[child_bag][parent_bag] = value
    return result


def main1(input_file) -> int:
    lines = load_input(input_file)
    bag_descriptions = {}
    for line in lines:
        bag_descriptions.update(read_bag_rule(line))
    dependencies = upstream_dependencies(bag_descriptions)
    holds_shiny_gold = set(dependencies["shiny gold"].keys())
    to_explore = set(dependencies["shiny gold"].keys())
    while to_explore:
        holder = to_explore.pop()
        new_dependencies = list(dependencies[holder].keys())
        holds_shiny_gold.update(new_dependencies)
        to_explore.update(new_dependencies)
    return len(holds_shiny_gold)


def main2(input_file):
    lines = load_input(input_file)
    bag_descriptions = {}
    for line in lines:
        bag_descriptions.update(read_bag_rule(line))
    pending_bags = [("shiny gold", 1),]
    count = -1
    while pending_bags:
        current_bag, times = pending_bags.pop()
        count += times
        for next_bag, next_times  in bag_descriptions[current_bag].items():
            pending_bag = (next_bag, times * next_times)
            pending_bags.append(pending_bag)
    return count
