FILE_NAME = "tower.txt"
TEST_NAME = "test_tower.txt"


class program_data():
    def __init__(self, name, weight, disc):
        self.name = name
        self.weight = weight
        self.disc = disc


def read_content(file_name):
    content = []
    with open(file_name, 'r') as file:
        for line in file.readlines():
            line = line.split()
            name = line[0]
            weight = int(line[1].replace("(", "").replace(")", ""))
            disc = []
            if len(line) > 2:
                index = 3
                while index < len(line):
                    disc.append(line[index].replace(",", ""))
                    index += 1
            content.append(program_data(name, weight, disc))
    return content


def who_is_on_bottom(content):
    """ 
        go trough the names in the list and check if any other name is holding him if not he is on bottom, that simple
    """
    for i in range(len(content)):
        current_name = content[i].name
        some_one_holding_me = False
        for check_to in range(len(content)):
            check_to_disc = content[check_to].disc
            for name in check_to_disc:
                if name == current_name:
                    some_one_holding_me = True
        if not some_one_holding_me:
            return current_name


def wrong_weight_solution_1(my_index, content):
    """
        the wrong weight one is the one who's weight is wrong compared to it's neightbors,
        AND it either doesn't hold anything(answer = neighbors_weight) 
        or the programs on it's disc are balanced(answer = my_weight - (my_overall_weight-neighbors_overall_weight))
    """
    my_weight = content[my_index].weight
    my_dics = content[my_index].disc
    my_overall_weight = get_weight(my_index, content)
    my_neighbors = get_neighbors(my_index, content)
    if len(my_neighbors) > 0:
        if i_am_the_wrong_weight_on_this_disk(my_overall_weight, my_neighbors, content):
            neighbors_overall_weight = get_weight(
                index_by_name(my_neighbors[0], content), content)
            if len(my_dics) == 0:
                answer = neighbors_overall_weight
                print(answer)
                return
            elif is_disc_balanced(my_dics, content):
                answer = my_weight - \
                    (my_overall_weight - neighbors_overall_weight)
                print(answer)
                return
    for program in my_dics:
        wrong_weight_solution_1(index_by_name(program, content), content)


def wrong_weight_solution_2(my_index,content):
    my_weight = content[my_index].weight
    my_dics = content[my_index].disc
    my_overall_weight = get_weight(my_index, content)
    my_neighbors = get_neighbors(my_index, content)

    if not is_disc_balanced(my_dics,content):
        for program in my_dics:
            wrong_weight_solution_2(index_by_name(program,content),content)
    else:
        if i_am_the_wrong_weight_on_this_disk(my_overall_weight, my_neighbors, content):
            neighbors_overall_weight = get_weight(
                index_by_name(my_neighbors[0], content), content)
            if len(my_dics) == 0:
                answer = neighbors_overall_weight
                print(answer)
                return
            elif is_disc_balanced(my_dics, content):
                answer = my_weight - \
                    (my_overall_weight - neighbors_overall_weight)
                print(answer)
                return


def i_am_the_wrong_weight_on_this_disk(myweight, neighbors, content):
    """ my weight is wrong if my neightbors weights match but my weight doesn't match my neighbor"""
    if is_disc_balanced(neighbors, content):
        first_neighbor_weight = get_weight(
            index_by_name(neighbors[0], content), content)
        if myweight != first_neighbor_weight:
            return True
    return False


def is_disc_balanced(disc, content):
    """ disc is balanced if all the programs on the disc have the same weight """
    weights = []
    for program in disc:
        weights.append(get_weight(index_by_name(program, content), content))
    return all_same(weights)


def all_same(items):
    return all(x == items[0] for x in items)


def get_neighbors(index, content):
    neightbors = []
    name = content[index].name
    for i in range(len(content)):
        if name in content[i].disc:
            neightbors = [x for x in content[i].disc]
            neightbors.remove(name)
            break
    return neightbors

def get_weight(index, content):
    weight = content[index].weight
    my_disc = content[index].disc
    if len(my_disc) > 0:
        for program in my_disc:
            weight += get_weight(index_by_name(program, content), content)
    return weight


def index_by_name(name, content):
    for i in range(len(content)):
        if content[i].name == name:
            return i


def main():

    content = read_content(FILE_NAME)
    test_content = read_content(TEST_NAME)

    bottom_name = who_is_on_bottom(content)
    bottom_name_test = who_is_on_bottom(test_content)

    print("part 1 answer: ")
    print(bottom_name)
    print("part 1 test answer: ")
    print(bottom_name_test)

    bottom_index = index_by_name(bottom_name, content)
    bottom_index_test = index_by_name(bottom_name_test, test_content)

    print("part 2 answer with first solution: ")
    wrong_weight_solution_1(bottom_index, content)
    print("part 2 test answer with first solution: ")
    wrong_weight_solution_1(bottom_index_test, test_content)

    print("part 2 answer with second solution: ")
    wrong_weight_solution_2(bottom_index, content)
    print("part 2 test answer with second solution: ")
    wrong_weight_solution_2(bottom_index_test, test_content)


if __name__ == "__main__":
    main()
