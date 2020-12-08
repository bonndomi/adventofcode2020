

def load_input(user_data_file):
    with open(user_data_file, "r") as fd:
        for line in fd:
            yield line.strip()

def get_instruction(line):
    command, _, times = line.partition(" ")
    return {command, int(times)}

def acc(position, accumulator, time):
    position += 1
    accumulator = accumulator + time
    return {position, accumulator}


def nop(position, accumulator):
    position += 1
    return {position, accumulator}


def jmp(position, accumulator, time):
    position = position + time
    return {position, accumulator}

def main1(input_file):
    lines = load_input(input_file)
    position = 0
    accumulator = 0
    been_there = []
    while position not in been_there:
        been_there.append(position)
        for line in lines:
            command, time = get_instruction(line)
            if command == "acc":
                position, accumulator = acc(position, accumulator, time)
                been_there.append(position)
            if command == "nop":
                position, accumulator = nop(position, accumulator)
                been_there.append(position)
            if command == "jmp":
                position, accumulator = jmp(position, accumulator, time)
                been_there.append(position)
    return {"position": position, "accumulator": accumulator}

def main2():
    pass
