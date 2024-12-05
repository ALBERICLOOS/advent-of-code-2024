def part1():
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

        if correct:
            result += int(update[int(len(update)/2)])
            print(result)
        print(f"update: {update}: {correct}")
    
    print(result)


part1()