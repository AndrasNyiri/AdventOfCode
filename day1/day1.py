FILE_NAME = "captcha.txt"

def read_content(file_name):
    with open(file_name, 'r') as file:
        for line in file.readlines():
            captcha_content = (str(line))
    captcha_content = list(captcha_content)
    for i in range(len(captcha_content)):
        captcha_content[i] = int(captcha_content[i])
    return captcha_content

def solve_catpcha(captcha_content,part = "part1"):
    if part == "part2":
        step = int(len(captcha_content)/2)
    else:
        step = 1
    matches = []
    for i in range(len(captcha_content)):
        next_check = i + step
        next_index = next_check % len(captcha_content)
        if captcha_content[i] == captcha_content[next_index]:
            matches.append(captcha_content[i])
    return sum(matches)


def main():
    content = read_content(FILE_NAME)
    print(solve_catpcha(content))
    print(solve_catpcha(content,"part2"))

if __name__ == "__main__":
    main()
