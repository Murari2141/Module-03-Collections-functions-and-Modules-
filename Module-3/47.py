def check(num,start,end) :
    if num >=start and num <=end :
        print("num in range")
    else :
        print("num not in range:")    

num = input("enter a num :")
num = int(num) 
start = 0
end = 9
res = check(num,start,end)
