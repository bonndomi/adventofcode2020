import dataclasses


def load_input(user_data_file):
    with open(user_data_file, "r") as fd:
        for line in fd:
            yield line.strip()



def acc(emulator):
    _, _, value = emulator.program[emulator.program_counter].partition(" ")
    emulator.program_counter += 1
    emulator.accumulator += int(value)


def nop(emulator):
    emulator.program_counter += 1


def jmp(emulator):
    _, _, value = emulator.program[emulator.program_counter].partition(" ")
    emulator.program_counter += int(value)


@dataclasses.dataclass
class Emulator:
    accumulator: int
    program: list[str]
    program_counter: int

    def execute_once(self):
        line = self.program[self.program_counter]
        if line.startswith("acc "):
            acc(self)
        elif line.startswith("nop "):
            nop(self)
        elif line.startswith("jmp "):
            jmp(self)

    def __iter__(self):
        return self

    def __next__(self):
        self.execute_once()
        return self


def main1(input_file):
    lines = load_input(input_file)
    been_there = {0}
    emulator = Emulator(accumulator = 0, program = list(lines), program_counter = 0)
    for _ in emulator:
        if emulator.program_counter in been_there:
            break
        been_there.add(emulator.program_counter)
    return emulator.accumulator

def main2(input_file):
    pass
