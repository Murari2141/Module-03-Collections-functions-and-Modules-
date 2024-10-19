num = {"a" : 1 ,"b" : 2 , "c" : 2 , "d" : 3 , "e" : 4, 'f' : 4, 'g' : 5} 
value = num.values()

res = []

for i in value :
    if i not in res :
        res.append(i)

print(res) 