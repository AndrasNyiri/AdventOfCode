FILE_NAME = "passphrases.txt"


def read_content(file_name):
    content = []
    with open(file_name, 'r') as file:
        for line in file.readlines():
            content.append(str(line).strip().split(" "))
    return content


def how_many_valid(content):
    count = 0
    for i in range(len(content)):
        valid = True
        for check_this in range(len(content[i])):
            for to_this in range(len(content[i])):
                if check_this != to_this and content[i][check_this] == content[i][to_this]:
                    valid = False
        if valid:
            count += 1
    return count


def how_many_valid_part2(content):
    count = 0
    for i in range(len(content)):
        valid = True
        for check_this in range(len(content[i])):
            for to_this in range(len(content[i])):
                if check_this != to_this and (content[i][check_this] == content[i][to_this] or is_anagram(content[i][check_this], content[i][to_this])):
                    valid = False
        if valid:
            count += 1
    return count


def is_anagram(word1, word2):
    return sort(word1) == sort(word2)

def sort(word):
    return sorted(word.lower().strip())

def main():
    content = read_content(FILE_NAME)
    print(how_many_valid(content))
    print(how_many_valid_part2(content))


if __name__ == "__main__":
    main()
