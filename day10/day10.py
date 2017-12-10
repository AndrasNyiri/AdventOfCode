FILE_NAME = "knot.txt"


def read_content_to_list(file_name):
    with open(file_name, 'r') as file:
        for line in file.readlines():
            return str(line).split(",")


def read_content_to_assci(file_name):
    with open(file_name, 'r') as file:
        for line in file.readlines():
            line = str(line).split(",")

    to_assci = []
    for char in line:
        for c in char:
            to_assci.append(ord(c))
        to_assci.append(ord(','))
    to_assci.pop()
    to_assci.extend([17, 31, 73, 47, 23])

    return to_assci


def twist_part1(lengths):
    numbers = list(range(256))
    current_position = 0
    skip_size = 0
    for length in lengths:
        length = int(length)
        sublist = []
        index = current_position
        count = 0
        while count < length:
            index = index % len(numbers)
            sublist.append(numbers[index])
            index += 1
            count += 1
        sublist.reverse()
        index = current_position
        count = 0
        while count < length:
            index = index % len(numbers)
            numbers[index] = sublist[count]
            index += 1
            count += 1
        current_position += length + skip_size
        current_position = current_position % len(numbers)
        skip_size += 1
    print("part 1 answer: ", numbers[0] * numbers[1])


def twist(numbers, lengths, current_position, skip_size, round_, maxround):
    for length in lengths:
        length = int(length)
        sublist = []
        index = current_position
        count = 0
        while count < length:
            index = index % len(numbers)
            sublist.append(numbers[index])
            index += 1
            count += 1
        sublist.reverse()
        index = current_position
        count = 0
        while count < length:
            index = index % len(numbers)
            numbers[index] = sublist[count]
            index += 1
            count += 1
        current_position += length + skip_size
        current_position = current_position % len(numbers)
        skip_size += 1
    round_ += 1
    if round_ != maxround:
        return twist(numbers, lengths, current_position, skip_size, round_, maxround)
    else:
        return numbers


def dense_to_hash(dense):
    final = ""
    for num in dense:
        final += to_hex(num)
    print("part 2 answer: ", final)


def sparse_to_dense(numbers):
    dense = []
    for j in range(16):
        sublist = []
        for i in range(16):
            sublist.append(numbers.pop(0))
        res = sublist[0] ^ sublist[1] ^ sublist[2] ^ sublist[3] ^ sublist[4] ^ sublist[5] ^ \
            sublist[6] ^ sublist[7] ^ sublist[8] ^ sublist[9] ^ sublist[10] ^ sublist[11] ^ \
            sublist[12] ^ sublist[13] ^ sublist[14] ^ sublist[15]
        dense.append(res)
    return dense


def to_hex(num):
    return hex(num).replace("0x", "")


def main():
    lenghts = read_content_to_list(FILE_NAME)
    twist_part1(lenghts)
    assci_lengths = read_content_to_assci(FILE_NAME)
    numbers = list(range(256))
    dense_to_hash(sparse_to_dense(twist(numbers, assci_lengths, 0, 0, 0, 64)))


if __name__ == "__main__":
    main()
