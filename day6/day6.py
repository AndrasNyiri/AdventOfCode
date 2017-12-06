FILE_NAME = "banks.txt"

def read_content(file_name):
    with open(file_name, 'r') as file:
        for line in file.readlines():
            content = [int(i) for i in (line.split('\t'))]
    return content


def debug(banks):
    iterations = 0
    visited = []
    while True:
        iterations += 1
        max_index, max_value = find_max(banks)
        banks[max_index] = 0
        while max_value > 0:
            max_index += 1
            if max_index == len(banks):
                max_index = 0
            banks[max_index] += 1
            max_value -= 1
        if banks in visited:
            return iterations
        else:
            temp_bank = [i for i in banks]
            visited.append(temp_bank)
    

def debug_part2(banks):
    iterations = 0
    visited = []
    while True:
        iterations += 1
        max_index, max_value = find_max(banks)
        banks[max_index] = 0
        while max_value > 0:
            max_index += 1
            if max_index == len(banks):
                max_index = 0
            banks[max_index] += 1
            max_value -= 1
        visited_ = is_in_visited(banks,visited)[0]
        when = is_in_visited(banks,visited)[1]
        if visited_:
            return iterations - when
        else:
            temp_bank = [i for i in banks]
            visited.append((temp_bank,iterations))

def is_in_visited(banks,visited):
    for i in range(len(visited)):
        if banks == visited[i][0]:
            return (True, i + 1)
    return (False,0)

def find_max(banks):
    max_index = 0
    max_value = 0
    for i in range(len(banks)):
        if max_value < banks[i]:
            max_value = banks[i]
    for i in range(len(banks)):
        if banks[i] == max_value:
            max_index = i
            break
    
    return (max_index,max_value)

def main():
    content = read_content(FILE_NAME)
    print(debug([0,2,7,0]))
    print(debug(content))
    content = read_content(FILE_NAME)
    print(debug_part2([0,2,7,0]))
    print(debug_part2(content))


if __name__ == "__main__":
    main()
