list = ('a','b','b','c','d','a','e','b','f')
list1 = []

for i in list :
    if i not in list1 :
        list1.append(i)
print(list1)