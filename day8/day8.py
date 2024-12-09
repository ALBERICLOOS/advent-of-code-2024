def part1():
    f = open("input.txt", "r")
    lines = f.readlines()

    coords_dict = dict()
    
    # tel vanaf 1!
    for line_idx in range(len(lines)):
        lines[line_idx] = lines[line_idx].strip()
        for idx, char in enumerate(lines[line_idx]):
            if char != ".":
                if char in coords_dict:
                    coords_dict[char].append((line_idx+1, idx+1))
                else:
                    coords_dict[char] = [(line_idx+1, idx+1)]

    antinodes = set()
    for key in coords_dict.keys():
        local_coords = coords_dict[key]
        for i in range(len(local_coords)):
            for j in range(len(local_coords)):
                if i != j:
                    row1, col1 = local_coords[i]
                    row2, col2 = local_coords[j]

                    row_diff = abs(row1 - row2)
                    col_diff = abs(col1 - col2)
                    
                    if row1 >= row2:
                        if col1 < col2: 
                            point1 = (row1 + row_diff, col1 - col_diff)
                            point2 = (row2 - row_diff, col2 + col_diff)
                        else:
                            point1 = (row2 - row_diff, col2 - col_diff)
                            point2 = (row1 + row_diff, col1+col_diff)
                    else:
                        if col1 < col2: 
                            point1 = (row1 - row_diff, col1 - col_diff)
                            point2 = (row2 + row_diff, col2 + col_diff)
                        else:
                            point1 = (row2 + row_diff, col2 - col_diff)
                            point2 = (row1 - row_diff, col1 + col_diff)

                    if point1[0] > 0 and point1[0] <= len(lines) and point1[1] > 0 and point1[1] <= len(lines[0]):
                        antinodes.add(point1)
                    if point2[0] > 0 and point2[0] <= len(lines) and point2[1] > 0 and point2[1] <= len(lines[0]):
                        antinodes.add(point2)

    print(coords_dict)
    print(len(antinodes))




# if it works it works :D
def part2():
    f = open("input.txt", "r")
    lines = f.readlines()

    coords_dict = dict()
    
    # tel vanaf 1!
    for line_idx in range(len(lines)):
        lines[line_idx] = lines[line_idx].strip()
        for idx, char in enumerate(lines[line_idx]):
            if char != ".":
                if char in coords_dict:
                    coords_dict[char].append((line_idx+1, idx+1))
                else:
                    coords_dict[char] = [(line_idx+1, idx+1)]

    antinodes = set()
    for key in coords_dict.keys():
        local_coords = coords_dict[key]
        for i in range(len(local_coords)):
            for j in range(len(local_coords)):
                if i != j:
                    row1, col1 = local_coords[i]
                    row2, col2 = local_coords[j]

                    row_diff = abs(row1 - row2)
                    col_diff = abs(col1 - col2)
                    
                    for k in range(100):
                        if row1 >= row2:
                            if col1 < col2: 
                                point1 = (row1 + row_diff*k, col1 - col_diff*k)
                                point2 = (row2 - row_diff*k, col2 + col_diff*k)
                            else:
                                point1 = (row2 - row_diff*k, col2 - col_diff*k)
                                point2 = (row1 + row_diff*k, col1+col_diff*k)
                        else:
                            if col1 < col2: 
                                point1 = (row1 - row_diff*k, col1 - col_diff*k)
                                point2 = (row2 + row_diff*k, col2 + col_diff*k)
                            else:
                                point1 = (row2 + row_diff*k, col2 - col_diff*k)
                                point2 = (row1 - row_diff*k, col1 + col_diff*k)

                        if point1[0] > 0 and point1[0] <= len(lines) and point1[1] > 0 and point1[1] <= len(lines[0]):
                            antinodes.add(point1)
                        if point2[0] > 0 and point2[0] <= len(lines) and point2[1] > 0 and point2[1] <= len(lines[0]):
                            antinodes.add(point2)

    print(coords_dict)
    print(len(antinodes))

part2()