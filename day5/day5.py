FILE_NAME = "jumps.txt"

def read_content(file_name):
    content = []
    with open(file_name, 'r') as file:
        for line in file.readlines():
            content.append(int(line))
    return content

def exit_maze(maze):
    steps = 0
    index = 0
    while True:
        steps += 1
        current_step = maze[index]
        maze[index] += 1
        index += current_step
        if index < 0 or index >= len(maze):
            break
    return steps

def exit_maze_part2(maze):
    steps = 0
    index = 0
    while True:
        steps += 1
        current_step = maze[index]
        if maze[index] >= 3:
            maze[index] -= 1
        else:
            maze[index] += 1
        index += current_step
        if index < 0 or index >= len(maze):
            break
    return steps


def main():
    content = read_content(FILE_NAME)
    print(exit_maze([0,3,0,1,-3]))
    print(exit_maze(content))

    content = read_content(FILE_NAME)
    print(exit_maze_part2([0,3,0,1,-3]))
    print(exit_maze_part2(content))


if __name__ == "__main__":
    main()
