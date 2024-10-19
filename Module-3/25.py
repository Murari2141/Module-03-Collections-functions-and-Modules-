num = [(1,2,3),(4,5,6),(7,8,9)]

replace_num = []
for t in num :
    temp = list(t)
    temp[-1] = 0
    replace_num.append(tuple(temp))
print(replace_num)
