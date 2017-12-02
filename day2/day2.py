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
    for k in range(len(content)):
        for i in range(len(content[k])):
            for j in range(len(content[k])):
                if i != j and content[k][i] % content[k][j] == 0:
                    num1 = content[k][i]
                    num2 = content[k][j]
                    division = num1 / num2
                    all_division.append(int(division))
    return(sum(all_division))

def main():
    content = read_content(FILE_NAME)
    print(solve_spreadsheet_part1(content))
    print(solve_spreadsheet_part2(content))

if __name__ == "__main__":
    main()
