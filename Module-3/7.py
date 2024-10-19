list1 = input("enter your list1 elements: ").split()
list2 = input("enter your list2 elements :").split()

for i in list1 :
    if i in list2 :
        result = True

print(result)