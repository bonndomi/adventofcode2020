import os

import pytest
from adventofcode import advent8


def test_advent8(user, user_data, record_testsuite_property):
    file = os.path.join(user_data, "8.txt")
    result = advent8.main1(file)
    record_testsuite_property(f"{user}-8-1", result)
    result = advent8.main2(file)
    record_testsuite_property(f"{user}-8-2", result)


@pytest.mark.parametrize(
    "input,execution_order,accumulator",
    (
            pytest.param(
                ["nop +0", "acc +1", "jmp +4", "acc +3", "jmp -3", "acc -99", "acc +1", "jmp -4", "acc +6"],
                [0, 1, 2, 6, 7, 3, 4, 1],
                5,
                id="example1"),
    ))
def test_execute_once(input, execution_order, accumulator):
    emulator = advent8.Emulator(accumulator=0, program=input, program_counter=0)

    assert emulator.program_counter == execution_order.pop(0)

    for expected_program_counter, _ in zip(execution_order, emulator):
        assert emulator.program_counter == expected_program_counter

    assert emulator.accumulator == accumulator
