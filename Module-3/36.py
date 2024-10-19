dict1 = {1 : "a" , 2 : "b" , 3 : "c" , 4 : "d" , 19 : "e" , 32 : "f" ,7 : "g" , -5 : "h"}

result = []

for keys , value in dict1.items() :
    if keys >= 1 and keys <= 15  :
        print(f"key {keys} : values {value}")

print(result)        

dict1 = { i : i**2 for i in range (1 , 16)}
print(dict1)
