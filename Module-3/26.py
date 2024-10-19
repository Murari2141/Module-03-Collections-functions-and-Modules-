tuple = (0,1,2,5,1,3,2,5,6,9,7,4,2)
repeated_value = []
seen_value = []

for item in tuple :
    if item in seen_value :
        if item not in repeated_value :
            repeated_value.append(item)
    else :
        seen_value.append(item)        
print(repeated_value)
