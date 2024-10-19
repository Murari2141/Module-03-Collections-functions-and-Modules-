num = [1,33,5,6,88,9,55,6,22,4,]

flag = False

while not flag :
    flag = True
    for index , i in enumerate(num) :
        if index < len(num)-1 :
            if num[index] > num[index+1] :
                num[index] , num[index+1]= num[index+1] , num[index]
                flag = False
            
         
print(num[1])
