import os

FILE_NAME = os.path.join(os.path.dirname(
    os.path.abspath(__file__)), "plumber.txt")

TEST_FILE_NAME = os.path.join(os.path.dirname(
    os.path.abspath(__file__)), "test_plumber.txt")


class Pipes():

    def __init__(self):
        self.pipes_list = []

    class Pipe():
        def __init__(self, id_, friends):
            self.id_ = id_
            self.friends = friends

    def add(self, id_, friends):
        self.pipes_list.append(self.Pipe(id_, friends))

    def index(self, index):
        return self.pipes_list[index]

    def length(self):
        return len(self.pipes_list)

    def index_by_id(self, id_):
        for i in range(len(self.pipes_list)):
            if self.pipes_list[i].id_ == id_:
                return i
        raise ValueError("There is no such ID")

    def get_friends(self, index):
        return self.pipes_list[index].friends


def read_content(test=False):
    file_name = TEST_FILE_NAME if test else FILE_NAME
    my_pipes = Pipes()
    with open(file_name, 'r') as file:
        for line in file.readlines():
            line = line.split()
            _id = line[0]
            friends = []
            for i in range(2, len(line)):
                friends.append(line[i].replace(',', ''))
            my_pipes.add(line[0], friends)
    return my_pipes


def get_friends_of_friend(pipes, id_):
    friends = [id_]
    get_friends(friends, pipes, id_)
    return friends


def get_friends(friends, pipes, id_):
    friend_index = pipes.index_by_id(id_)
    new_friends = []
    for friend in pipes.get_friends(friend_index):
        if friend not in friends:
            friends.append(friend)
            new_friends.append(friend)
    if len(new_friends) > 0:
        for new_friend in new_friends:
            get_friends(friends, pipes, new_friend)

def get_groups(pipes):
    groups = []
    for i in range(pipes.length()):
        if not in_groups(groups,pipes.index(i).id_):
            groups.append(get_friends_of_friend(pipes,pipes.index(i).id_))
    return len(groups)



def in_groups(groups,id_):
    for group in groups:
        if id_ in group:
            return True
    return False

def main():
    my_pipes = read_content(False)
    print(len(get_friends_of_friend(my_pipes, '0')))
    print(get_groups(my_pipes))


if __name__ == "__main__":
    main()
