def check_x_mas(string):
    if string == "XMAS" or string == "SAMX":
        return True
    return False

def copy(row, column):
    result = []
    for _ in range(row):
        temp = []
        for _ in range(column):
            temp.append(".")
        result.append(temp)
    return result


def part1():
    f = open("input.txt", "r")
    lines = f.readlines()
    lines = [line.strip() for line in lines]

    copy_matrix = copy(len(lines), len(lines[0]))

    horizontal_amount = 0

    for i in range(len(lines)): #check horizontal
        line = lines[i]
        for j in range(len(line) - 3): 
            string = line[j:j+4]
            if check_x_mas(line[j:j+4]):
                horizontal_amount += 1
                copy_matrix[i][j:j+4] = string
        
    vertical_amount = 0

    for i in range(len(lines)-3):  # check vertical
        for j in range(len(lines[i])):
            string = ''.join(lines[i+k][j] for k in range(4))
            if check_x_mas(string):
                for k in range(4):
                    copy_matrix[i+k][j] = string[k]
                vertical_amount += 1

    diagonal_amount = 0
    for i in range(len(lines)-3):
        for j in range(len(lines[i])-3):
            string = ''.join(lines[i+k][j+k] for k in range(4))
            if check_x_mas(string):
                for k in range(4):
                    copy_matrix[i+k][j+k] = string[k]
                diagonal_amount += 1
            
    for i in range(len(lines)-3):
        for j in range(3, len(lines[i])):
            string = ''.join(lines[i+k][j-k] for k in range(4))
            if check_x_mas(string):
                for k in range(4):
                    copy_matrix[i+k][j-k]  = string[k]
                diagonal_amount += 1

    amount = horizontal_amount + vertical_amount + diagonal_amount
    print(amount)

    for row in copy_matrix:
        print("".join(row))


def check_mas(string):
    if string == "MAS" or string == "SAM":
        return True
    return False

def part2():
    f = open("input.txt", "r")
    lines = f.readlines()
    lines = [line.strip() for line in lines]

    copy_matrix = copy(len(lines), len(lines[0]))

    amount = 0

    for i in range(1, len(lines)-1):
        for j in range(1, len(lines[i])-1):
            string1 = ''.join(lines[i+k][j+k] for k in range(-1, 2, 1))
            string2 = ''.join(lines[i+k][j-k] for k in range(-1, 2, 1))
            if check_mas(string1) and check_mas(string2):
                for k in range(-1, 2, 1):
                    copy_matrix[i+k][j+k] = string1[1+k]
                    copy_matrix[i+k][j-k] = string2[1+k]
                amount += 1

    for row in copy_matrix:
        print("".join(row))
    print(amount)

part2()