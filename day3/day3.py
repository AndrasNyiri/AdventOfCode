UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)


def create_sprial(max_value, part2 = False, width = 610, height = 610):
    turn_left = {UP : LEFT, LEFT : DOWN, DOWN : RIGHT, RIGHT : UP}
    spiral = [[None] * width for _ in range(height)]
    direction_x, direction_y = DOWN
    x = width // 2
    y = height // 2
    count = 0
    start = (x, y)
    while True:
        count += 1
        if part2:
            spiral[y][x] = sum_of_neighbors(spiral,x,y,width,height)
            if spiral[y][x] > max_value:
                print("first value written that is larger than the max_value: " , spiral[y][x])
                return spiral
        else:
            spiral[y][x] = count
        new_direction_x , new_direction_y = turn_left[direction_x,direction_y]
        new_x, new_y = x + new_direction_x, y + new_direction_y
        if(0 <= new_x < width and 0 <= new_y < height and
            spiral[new_y][new_x] is None and count != max_value):
            x, y = new_x, new_y
            direction_x, direction_y = new_direction_x, new_direction_y
        else:
            if not (0 <= x < width and 0 <= y < height) or count == max_value:
                end = (x, y)
                manhattan_distance = (abs(start[0] - end[0]) + abs(start[1] - end[1]))
                print("count: " , count)
                print("manhattan_distance: " , manhattan_distance)
                return spiral
            x, y = x + direction_x, y + direction_y

def sum_of_neighbors(spiral,x,y,width,height):
    sum_ = 0
    if y + 1 < height and spiral[y + 1][x] != None:
        sum_ += spiral[y + 1][x]
    if y - 1 >= 0 and spiral[y - 1][x] != None:
        sum_ += spiral[y - 1][x]
    if x + 1 < width and spiral[y][x + 1] != None:
        sum_ += spiral[y][x + 1]
    if x - 1 >= 0 and spiral[y][x - 1] != None:
        sum_ += spiral[y][x - 1]
    if y + 1 < height and x + 1 < width and spiral[y + 1][x + 1] != None:
        sum_ += spiral[y + 1][x + 1]
    if y - 1 >= 0 and x + 1 < width and spiral[y - 1][x + 1] != None:
        sum_ += spiral[y - 1][x + 1]
    if y - 1 >= 0 and x - 1 >= 0 and spiral[y - 1][x - 1] != None:
        sum_ += spiral[y - 1][x - 1]
    if y + 1 < height and x - 1 >= 0 and spiral[y + 1][x - 1] != None:
        sum_ += spiral[y + 1][x - 1]
    if sum_ == 0:
        return 1
    else:
        return sum_


def main():
    create_sprial(1)
    create_sprial(12)
    create_sprial(23)
    create_sprial(1024)
    create_sprial(368078)
    create_sprial(368078,True)

if __name__ == "__main__":
    main()