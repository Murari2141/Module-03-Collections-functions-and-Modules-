list1 = [1,2,2,3,4,5,5,6,5,4,3,2,6,7,8,9]

unique = []

for i in list1:
    if i not in unique:
        unique.append(i)

print("Unique value is : ",unique)
