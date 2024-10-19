dict = {'a': 3, 'b': 4, 'c': 1, 'd': 2}

asc = {}
des = {}

for key in sorted(dict,key=dict.get):
    asc[key] = dict[key]
print(asc)  

for key in sorted(dict,key=dict.get,reverse=True):
    des[key] = dict[key]
print(des)
