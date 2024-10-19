chs = {
    'a': 10,
    'b': 20,
    'c': 40,
    'd': 50
}

check = ("a","b","d")

flag = True

for c in check :
    if c not in chs :
        flag = False
        break

if flag:
    print("key exist in dictionary")
else:
    print("given key is not exist in dictionary")
    
    