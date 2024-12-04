import re


def algo(line):
    x = re.findall("mul\([0-9]{1,3},[0-9]{1,3}\)", line)

    total = 0

    for seq in x:
        seq = seq[4: -1]
        seq = seq.split(",")
        total += (int(seq[0]) * int(seq[1]))
    return total

def part1():
    f = open("input.txt", "r")
    line = " ".join(f.readlines())
    
    total = algo(line)
    print(total)



def part2():
    f = open("input.txt", "r")
    line = " ".join(f.readlines())
    
    do_not = line.split("don't()")

    total = 0
    total += algo(do_not[0])


    for l in do_not[1:]:
        dos = l.split("do()")[1:]
        for do in dos:
            total += algo(do)

    print(total)

part2()
