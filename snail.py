def snail(snail_map):
    size = len(snail_map[0])
    aux = 0
    res = list()
    while size > 0:
        # Top Row
        res.extend(snail_map[aux][aux:size-1])
        # Rigth Col
        res.extend([r[size-1] for r in snail_map[aux:size-1]])
        # Bottom Row
        res.extend(snail_map[size-1][::-1][aux:size-1])
        # Left Col
        res.extend([r[aux] for r in snail_map[::-1][aux:size-1]])
        # Center
        if aux == size-1:
            res.append(snail_map[aux][size-1])
            break
        size -= 1
        aux += 1
    
    return res




array = [[1,2,3],
         [8,9,4],
         [7,6,5]]    

expected = [1,2,3,4,5,6,7,8,9]
print(snail(array))
assert (snail(array) == expected)
