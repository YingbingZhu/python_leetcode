path = [1, 2, 4, 6, 9, 13, 14 ,15]
queries = [2,5,16]
res = []
for num in queries:
    l = 0
    curr = [-1, -1]
    while l < len(path) and path[l] < num:
        l += 1
        print(l)
    if l < len(path) and path[l] <= num:
        curr[0] = path[l]
    res.append(curr)

print(res)
