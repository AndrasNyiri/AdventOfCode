FILE_NAME = "steps.txt"


def read_content_to_list(file_name):
    with open(file_name, 'r') as file:
        for line in file.readlines():
            return str(line).split(",")

def shortest_path(steps):
    restart = True
    while restart:
        restart = shorten_all_steps(steps)
    
    shortest_steps = len(steps)
    return shortest_steps
    """
    print("shorest steps: ",shortest_steps)
    print("")
    """

def max_path(steps):
    max_path_ = 0
    steps_one_by_one = []
    for i in range(len(steps)):
        steps_one_by_one.append(steps[i])
        shortest_steps = shortest_path(steps_one_by_one)
        if shortest_steps > max_path_:
            max_path_ = shortest_steps
    return max_path_




def shorten_all_steps(steps):
    for j in range(len(steps)):
            for k in range(len(steps)):
                step1 = steps[j]
                step2 = steps[k]
                short = shorten_two_steps(step1,step2)
                if short != None:
                    if short == "del":
                        steps.pop(k)
                        steps.pop(j)
                    else:
                        steps[j] = short
                        steps.pop(k)
                    return True
    return False

def shorten_two_steps(step1, step2):
    if step1 == "ne":
        if step2 == "s":
            return "se"
        elif step2 == "nw":
            return "n"
        elif step2 == "sw":
            return "del"

    elif step1 == "se":
        if step2 == "n":
            return "ne"
        elif step2 == "sw":
            return "s"
        elif step2 == "nw":
            return "del"

    elif step1 == "s":
        if step2 == "ne":
            return "se"
        elif step2 == "nw":
            return "sw"
        elif step2 == "n":
            return "del"
        

    elif step1 == "sw":
        if step2 == "se":
            return "s"
        elif step2 == "n":
            return "nw"
        elif step2 == "ne":
            return "del"

    elif step1 == "nw":
        if step2 == "s":
            return "sw"
        elif step2 == "ne":
            return "n"
        elif step2 == "se":
            return "del"

    elif step1 == "n":
        if step2 == "se":
            return "ne"
        elif step2 == "sw":
            return "nw"
        elif step2 == "s":
            return "del"

    return None


def main():
    """content = read_content_to_list(FILE_NAME)
    shortest_path(["ne", "ne", "ne"])
    shortest_path(["ne", "ne", "sw","sw"])
    shortest_path(["ne", "ne", "s","s"])
    shortest_path(["se", "sw", "se","sw","sw"])
    shortest_path(content)
    """
    content = read_content_to_list(FILE_NAME)
    print(max_path(content))


if __name__ == "__main__":
    main()
