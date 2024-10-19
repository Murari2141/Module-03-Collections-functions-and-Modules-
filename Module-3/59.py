num = int(input("enter a number value :"))

sum = 0

for i in range(1,num // 2 +1):
    if num % i == 0 :
        sum += i

sum += num

print(sum)