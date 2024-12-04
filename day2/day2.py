def is_save(string):
    increasing = False
    decreasing = False
    safe = True

    for i in range(len(string)-1):
        first = int(string[i])
        second = int(string[i+1])

        if(first > second):
            decreasing = True
        elif (first < second):
            increasing = True

        if (abs(first - second) > 3 or  first == second):
            safe = False
    
    if (increasing and decreasing):
        safe = False

    return safe



def part1(): 
    f = open("input.txt", "r")
    lines = f.readlines()

    amount = 0

    for line in lines:
        splitted = line.split()

        safe = is_save(splitted)
        if safe:
            amount += 1

    print(amount)


def part2(): 
    f = open("input.txt", "r")
    lines = f.readlines()

    amount = 0

    for line in lines:
        splitted = line.split()

        if is_save(splitted):
            amount+= 1
        else:
            safe_amount = 0
            for j in range(len(splitted)):

                temp = splitted[:j] + splitted[j+1:]
                
                if is_save(temp):
                    safe_amount+=1

            if safe_amount > 0:
                amount+= 1
    print(amount)

part2()