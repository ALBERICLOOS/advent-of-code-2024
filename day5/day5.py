import copy


def part1():
    f = open("test.txt", "r")

    before = dict() # stores values that need to be before key

    line = f.readline()
    while(line != "\n"):
        splitted = line.strip().split("|")
        first, second = splitted[0], splitted[1]
        
        if second in before:
            before[second].append(first)
        else:
            before[second] = [first]
        line = f.readline()

    updates = f.readlines()
    result = 0

    for update in updates:
        correct = True
        update = update.strip().split(",")

        for i in range(len(update)):
            if update[i] in before:
                for value in before[update[i]]:
                    if value in update[i:]:
                        correct = False

        if correct:
            result += int(update[int(len(update)/2)])
            print(result)
        print(f"update: {update}: {correct}")
    
    print(result)


def make_correct(update, before):

    result = []

    # only store items in dict that are also in update
    rules = {}
    for value in update:
        if value in before:
            rules[value] = []
            for item in before[value]:
                if item in update:
                    rules[value].append(item)
        else:
            rules[value] = []

    while len(update) > 0:
        for key in rules:
            if str(key) in update and rules[key] == []:
                result.append(key)
                update.remove(key)
                for value in rules:
                    if key in rules[value]:
                        rules[value].remove(key)
    return result
                



def part2():
    # yoink code from part 1
    f = open("input.txt", "r")

    before = dict() # stores values that need to be before key

    line = f.readline()
    while(line != "\n"):
        splitted = line.strip().split("|")
        first, second = splitted[0], splitted[1]
        
        if second in before:
            before[second].append(first)
        else:
            before[second] = [first]
        line = f.readline()

    updates = f.readlines()
    result = 0

    for update in updates:
        correct = True
        update = update.strip().split(",")

        for i in range(len(update)):
            if update[i] in before:
                for value in before[update[i]]:
                    if value in update[i:]:
                        correct = False

        if not correct:
            corrected = make_correct(update, before)
            result += int(corrected[int(len(corrected)/2)])

    print(result)
part2()
