str = 'py5hon jfn5g'

dict = {}

for i in str :
    if i in dict:
        dict[i] += 1
    else :
        dict[i] = len(i)


print(dict)