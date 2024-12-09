from math import floor


def part1():
    f = open("input.txt", "r")
    lines = f.readlines()

    results = []

    for line in lines:
        line = line.split(" ")
        outcome = int(line[0][:-1])

        temp_results = [int(line[1])]
        
        for index, number in enumerate(line[2:]):
            number = int(number)
            amount_of_rounds = pow(2,index)

            for _ in range(amount_of_rounds):
                parent = temp_results[floor((len(temp_results)-1)/2)]
                temp_results.append(parent+number)
                temp_results.append(parent*number)

        if outcome in temp_results:
            results.append(outcome)

    result = 0
    for res in results:
        result += res
    print(result)



def part2():
    f = open("input.txt", "r")
    lines = f.readlines()

    results = []

    for line in lines:
        line = line.split(" ")
        outcome = int(line[0][:-1])

        temp_results = [int(line[1])]
        
        for number in line[2:]:
        
            number = int(number)
            temp_sums = []
            for item in temp_results:
                temp_sums.append(item + number)
                temp_sums.append(item * number)
                temp_sums.append(int(str(item) + str(number)))
            temp_results = temp_sums
        
        if outcome in temp_results:
            results.append(outcome)

    result = 0
    for res in results:
        result += res
    print(result)

part2()