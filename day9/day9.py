def part1():
    f = open("input.txt", "r")
    line = f.readline().strip()

    id = 0
    files = True
    diskmap = []

    # step 1
    for number in line:
        if files:
            for _ in range(int(number)):
                diskmap.append(id)
            id += 1
        else:
            for _ in range(int(number)):
                diskmap.append(".")
        files = not files
    
    #print(diskmap)
    
    # step 2
    amount_of_dots = 0
    for i in range(len(diskmap)):
        if diskmap[i] == ".":
            amount_of_dots += 1

    start = 0
    for i in range(len(diskmap)-1, len(diskmap) -1 - amount_of_dots, -1):
        for j in range(start, len(diskmap) - amount_of_dots):
            if diskmap[i] != "." and diskmap[j] == ".":
                diskmap[j] = diskmap[i]
                diskmap[i] = "."
                start = j
            
    #step 3
    checksum = 0
    for i in range(len(diskmap) - amount_of_dots):
        checksum += i * diskmap[i]

    print(checksum)

def part2():
    f = open("input.txt", "r")
    line = f.readline().strip()

    id = 0
    files = True
    diskmap = []

    # step 1
    for number in line:
        if files:
            for _ in range(int(number)):
                diskmap.append(id)
            id += 1
        else:
            for _ in range(int(number)):
                diskmap.append(".")
        files = not files
    
    
    # step 2
    amounts = []
    indices = []
    for index, value in enumerate(diskmap):
        if value != ".":
            if value >= len(amounts):
                amounts.append(1)
                indices.append(index)
            else:
                amounts[value] += 1

    lengths = amounts.copy()

    index = 0
    while index < len(diskmap):
        start = index
        while diskmap[start] == diskmap[index] and diskmap[index] == ".":
            start += 1

        
        if start != index:
            length = start - index
            for i in range(len(amounts)-1, -1, -1):
                if amounts[i] <= length and amounts[i] != 0:
                    for j in range(amounts[i]):
                        diskmap[index + j] = i
                    amounts[i] = 0
                    break
        index += 1

    #step 3
    checksum = 0
    for i in range(len(diskmap)):
        if diskmap[i] != ".":
            if lengths[diskmap[i]] > 0:
                checksum += i * diskmap[i]
                lengths[diskmap[i]]-= 1

    print(checksum)
    print(len(diskmap))

        

part2()