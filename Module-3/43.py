fruits = {
    'apple': 10,
    'banana': 20,
    'cherry': 30,
    'Orange': 40,
}

values = sorted(fruits.values())

v = values[-1:-4:-1]

print(v)

keys = sorted(fruits.keys())

k = keys[-1:-4:-1]

print(k)

result = list(zip(k,v))
print(result)