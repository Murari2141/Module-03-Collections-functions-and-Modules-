def uniele(list):
    unielelist = []
    for i in list:
        if i not in unielelist:
            unielelist.append(i)
    return unielelist        
    
list1 = [1,2,2,3,4,5,5,6,5,4,3,2,6,7,8,9]    
res = uniele(list1)
print("Unique elements is : ",res)
