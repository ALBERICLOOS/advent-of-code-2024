

def part1(): 
    f = open("input.txt", "r")
    lines = f.readlines()
    list1 = []
    list2 = []

    for line in lines:
        splitted = line.split()
        list1.append(int(splitted[0]))
        list2.append(int(splitted[1]))

    list1.sort()
    list2.sort()

    distance = 0

    for i in range(len(list1)):
        distance += abs(list1[i] - list2[i])

    print(distance)



def part2():
    f = open("input.txt", "r")
    lines = f.readlines()
    list1 = []
    list2 = []

    for line in lines:
        splitted = line.split()
        list1.append(int(splitted[0]))
        list2.append(int(splitted[1]))

    amount = dict()
    for number in list2:
        if number in amount:
            amount[number] += 1
        else:
            amount[number] = 1
    
    similarity = 0
    for number in list1:
        if number in amount:
            similarity += (number * amount[number])

    print(similarity)

part2()