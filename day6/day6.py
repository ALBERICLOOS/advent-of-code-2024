def print_map(map):
    for line in map:
        print("".join(line))


def part1():
    f = open("input.txt", "r")
    map = f.readlines()

    guard_position = [0, 0] # row, col
    width = len(map[0])
    height = len(map)

    # init the map
    for i in range(len(map)):
        found = map[i].find("^")
        if  found > -1:
            guard_position[0], guard_position[1] = i, found
        map[i] = list(map[i].rstrip())

    # search the players position

    finished = False

    while not finished:
        row, col = guard_position[0], guard_position[1]
        if map[row][col] == "^" and row -1 >= 0:
            if map[row-1][col] == "#":
                map[row][col] = ">"
            else:
                map[row][col] = "X"
                map[row-1][col] = "^"
                guard_position[0] = row - 1
        # go right
        elif map[row][col] == ">" and col + 1 < width:
            if map[row][col + 1] == "#":
                map[row][col] = "v"
            else:
                map[row][col] = "X"
                map[row][col+1] = ">"
                guard_position[1] = col+1
        # go down
        elif map[row][col] == "v" and row + 1 < height:
            if map[row + 1][col] == "#":
                map[row][col] = "<"
            else:
                map[row][col] = "X"
                map[row+1][col] = "v"
                guard_position[0] = row + 1
        # go left
        elif map[row][col] == "<" and col - 1 >= 0:
            if map[row][col - 1] == "#":
                map[row][col] = "^"
            else:
                map[row][col] = "X"
                map[row][col - 1] = "<"
                guard_position[1] = col - 1
        else:
            map[row][col] = "X"
            finished = True

    amount = 0
    for i in range(len(map)):
        for j in range(len(map[i])):
            if map[i][j] == "X":
                amount += 1
    print(guard_position)
    print_map(map)
    print(amount)


part1()