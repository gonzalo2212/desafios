def snail(snail_map):
    size = len(snail_map[0])
    col = row = 0
    reversa = False
    res = list()
    while size > 0:
        if not reversa:
            if col < size-1:
                res.append(snail_map[row][col])
                col += 1
            elif row < size:
                res.append(snail_map[row][col])
                row += 1
            else:
                size = size-1
                row -= 1
                col -= 1
                reversa = True
        else:
            if col >= len(snail_map)-size:
                res.append(snail_map[row][col])
                col -= 1
            elif row >= len(snail_map)-size:
                res.append(snail_map[row][col])
                row -= 1
            else:
                col += 1
                row += 1
                reversa = False
    
    return res




array = [[1,2,3],
         [8,9,4],
         [7,6,5]]
expected = [1,2,3,4,5,6,7,8,9]
print(snail(array))
assert (snail(array) == expected)
