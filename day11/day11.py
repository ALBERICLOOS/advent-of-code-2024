
def part1():
    f = open("input.txt", "r")
    line = f.readline().strip().split(" ")
    print(line)

    amount_of_blinks = 75
    new_line = []
    for i in range(amount_of_blinks):
        print(i)
        for item in line:
            if int(item) == 0:
                new_line.append(1)
            elif len(str(item))%2 == 0:
                half = int(len(str(item))/2)
                first = int(str(item)[:half])
                second = int(str(item)[half:])
                new_line.append(first)
                new_line.append(second)
            else:
                new_line.append(int(item) * 2024)
        line = new_line
        new_line = []
    print(len(line))


def next_state(stone_counts):
    new_counts = {}
    
    for stone, count in stone_counts.items():
        if stone == 0:
            if 1 in new_counts:
                new_counts[1] += count
            else:
                new_counts[1] = count
        else:
            stone_str = str(stone)
            digits = len(stone_str)

            if digits % 2 == 0:
                half = digits // 2
                left = int(stone_str[:half])
                right = int(stone_str[half:])
                if left in new_counts:
                    new_counts[left] += count
                else:
                    new_counts[left] = count
                if right in new_counts:
                    new_counts[right] += count
                else:
                    new_counts[right] = count
            else: 
                new_stone = stone * 2024
                if new_stone in new_counts:
                    new_counts[new_stone] += count
                else:
                    new_counts[new_stone] = count

    return new_counts


def part2():
    f = open("input.txt", "r")
    line = list(map(int, f.readline().strip().split(" ")))

    amount_of_blinks = 75


    stone_counts = {}
    for number in line:
        if number in stone_counts:
            stone_counts[number] += 1
        else:
            stone_counts[number] = 1

    for _ in range(amount_of_blinks):
        stone_counts = next_state(stone_counts)
    
    print(sum(stone_counts.values()))

part2()