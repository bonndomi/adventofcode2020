

def load_input(user_data_file):
    with open(user_data_file, "r") as fd:
        for line in fd:
            strip = line.strip()
            if not strip:
                continue
            yield strip


def get_seat(seat: str) -> int:
    return int(seat.replace("F", "0").replace("B", "1").replace("L", "0").replace("R", "1"), 2)

def main1(input_file):
    coordinates = load_input(input_file)
    max_seat_id = max(get_seat(s) for s in coordinates)
    return max_seat_id


def min_max_sum(seats) -> tuple[int, int, int]:
    min_row = None
    max_row = None
    min_row_sum = 0
    max_row_sum = 0
    seat_sum = 0
    for seat in seats:
        row = seat // 8
        if min_row is None:
            min_row = row
            max_row = row
        if row == min_row:
            min_row_sum += seat
        if row == max_row:
            max_row_sum += seat
        if row < min_row:
            min_row_sum = seat
            min_row = row
        if row > max_row:
            max_row_sum = seat
            max_row = row
        seat_sum += seat
    seat_sum = seat_sum - min_row_sum - max_row_sum
    return min_row, max_row, seat_sum


def main2(input_file):
    coordinates = load_input(input_file)
    min_row, max_row, seat_sum = min_max_sum(get_seat(s) for s in coordinates)
    possible_total = sum(range((min_row + 1) * 8, (max_row -1) * 8))
    return possible_total - seat_sum

