import os
import time
import copy

FILE_NAME = os.path.join(os.path.dirname(
    os.path.abspath(__file__)), "packet.txt")

TEST_FILE_NAME = os.path.join(os.path.dirname(
    os.path.abspath(__file__)), "test_packet.txt")


def read_content(test=False):
    file_name = TEST_FILE_NAME if test else FILE_NAME
    trip = []
    layers = []
    with open(file_name, 'r') as file:
        for line in file.readlines():
            line = line.split()
            depth = int(line[0].replace(':', ''))
            range_ = int(line[1])
            layers.append((depth, range_))
    index = 0
    last_depth = layers[-1][0]
    for i in range(last_depth + 1):
        range_ = index_in_layers(i, layers)
        if range_ != None:
            layer = [None] * range_
            # Scanner : ('S',direction) direction = 'u' or 'd', default is down
            layer[0] = ('S', 'd')
        else:
            layer = []
        trip.append(layer)
    return trip


def index_in_layers(index, layers):
    for layer in layers:
        if index == layer[0]:
            return layer[1]
    return None


def move_scanners(trip):
    for i in range(len(trip)):
        layer = trip[i]
        if len(layer) > 0:
            index, direction = get_scanner_index(layer)
            scanner = layer[index]
            layer[index] = None
            if direction == 'u':
                if index - 1 >= 0:
                    layer[index - 1] = scanner
                else:
                    layer[index + 1] = ('S', 'd')
            else:
                if index + 1 < len(layer):
                    layer[index + 1] = scanner
                else:
                    layer[index - 1] = ('S', 'u')


def get_scanner_index(layer):
    for i in range(len(layer)):
        if layer[i] != None:
            return i, layer[i][1]


def calculate_severity(trip,calculate):
    packet_pos = 0
    severity = 0
    escaped = True
    for i in range(len(trip)):
        if len(trip[i]) > 0 and trip[i][0] != None:
            if calculate:
                severity += (i * len(trip[i]))
            else:
                escaped = False
                break
            
        packet_pos += 1
        move_scanners(trip)
    return severity, escaped


#on top when delay % range + (range - 2) == 0

def delays_to_wait(original_trip):
    delays = 0
    while True:
        if not caught_in_delay(original_trip,delays):
            break
        delays += 1
    return delays

def caught_in_delay(trip, delay):
    step = delay
    for layer in trip:
        range_ = len(layer)
        if range_ > 0:
            if step % ((range_ - 1) * 2) == 0:
                return True
        step += 1
    return False
    

def main():
    trip = read_content(False)
    #print(calculate_severity(copy.deepcopy(trip),True))
    print(delays_to_wait(trip))


if __name__ == "__main__":
    main()
