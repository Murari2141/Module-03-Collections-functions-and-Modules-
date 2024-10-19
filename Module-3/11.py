list = ["abc" , "aba" , "cc" , "xyz" , "dd" ,"asd"]

count = 0

for i in list :
    if len(i) >= 2 and i[0] == i[-1] :
        count += 1
print(count)    