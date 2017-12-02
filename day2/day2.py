FILE_NAME = "spreadsheet.txt"

def read_content(file_name):
    content = []
    with open(file_name, 'r') as file:
        for line in file.readlines():
            line = str(line).split("\t")
            for i in range(len(line)):
                line[i] = int(line[i])
            content.append(line)
    return content

def solve_spreadsheet_part1(content):
    all_diffs = []
    for i in range(len(content)):
        _min = min(content[i])
        _max = max(content[i])
        diff = _max - _min
        all_diffs.append(diff)
    return sum(all_diffs)

def solve_spreadsheet_part2(content):
    all_division = []
    for all_ in range(len(content)):
        for check_this in range(len(content[all_])):
            for to_this in range(len(content[all_])):
                if check_this != to_this and content[all_][check_this] % content[all_][to_this] == 0:
                    num1 = content[all_][check_this]
                    num2 = content[all_][to_this]
                    division = num1 / num2
                    all_division.append(int(division))
    return(sum(all_division))

def main():
    content = read_content(FILE_NAME)
    print(solve_spreadsheet_part1(content))
    print(solve_spreadsheet_part2(content))

if __name__ == "__main__":
    main()
