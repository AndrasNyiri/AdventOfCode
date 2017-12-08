import operator

FILE_NAME = "registers.txt"

def read_registers(file_name):
    registers = {}
    with open(file_name, 'r') as file:
        for line in file.readlines():
            line = line.split()
            register_1 = line[0]
            register_2 = line[4]
            if register_1 not in registers:
                registers[register_1] = 0
            if register_2 not in registers:
                registers[register_2] = 0
    return registers


class instruct_info():
    def __init__(self, register_to_change, command, value, register_to_check, condition, condition_value):
        self.register_to_change = register_to_change
        self.command = command
        self.value = value
        self.register_to_check = register_to_check
        self.condition = condition
        self.condition_value = condition_value


def read_instructions(file_name):
    instructions = []
    with open(file_name, 'r') as file:
        for line in file.readlines():
            line = line.split()
            instructions.append(instruct_info(
                line[0],
                line[1],
                int(line[2]),
                line[4],
                line[5],
                int(line[6])
            ))
    return instructions


def do_instructions(registers, instructions):
    max_ever = 0
    for i in range(len(instructions)):
        condition = '{} {} {}'.format("registers[instructions[i].register_to_check]",
                                      instructions[i].condition,
                                      "instructions[i].condition_value")
        if eval(condition):
            if instructions[i].command == "inc":
                registers[instructions[i].register_to_change] += instructions[i].value
            else:
                registers[instructions[i].register_to_change] -= instructions[i].value
        
        current_max =  max(registers.values())
        if current_max > max_ever:
            max_ever = current_max

    print(current_max)
    print(max_ever)


def main():
    registers = read_registers(FILE_NAME)
    instructions = read_instructions(FILE_NAME)
    do_instructions(registers,instructions)


if __name__ == "__main__":
    main()
