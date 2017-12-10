FILE_NAME = "stream.txt"

def read_content(file_name):
    with open(file_name, 'r') as file:
        for line in file.readlines():
            return list(line)

def get_group_count(stream):
    count = 0
    stream = remove_character_after_exclamation_mark(stream)
    stream = remove_garbage(stream)
    #print(stream)

    index = 0
    score = 0
    while index < len(stream):
        if stream[index] == '{':
            score += 1
        
        if stream[index] == '}':
            count += score
            score -= 1
        index += 1

    return count

def remove_character_after_exclamation_mark(stream):
    index = 0
    while index < len(stream) - 1:
        if stream[index] == '!':
            stream.pop(index)
            stream.pop(index)
        else:
            index += 1
    return stream

def remove_garbage(stream):
    index = 0
    garbage_count = 0
    while index < len(stream):      
        if stream[index] == '<':
            end_found = False
            start_index = index
            while not end_found and index < len(stream):
                index += 1
                if stream[index] == '>':
                    end_found = True
                else:
                    garbage_count += 1
            if end_found:
                for i in range(start_index,index + 1):
                    stream.pop(start_index)
            index = start_index
        else:
            index += 1
    print("garabe count: ", garbage_count)
        
    return stream


def main():
    stream = read_content(FILE_NAME)
    print(get_group_count(stream))



if __name__ == "__main__":
    main()
