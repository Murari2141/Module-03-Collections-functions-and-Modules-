fruits = {
    'apple': 10,
    'banana': 20,
    'Mango': 40,
    'Orange': 50
}

check = input("Enter Fruits name :")

if fruits.get(check) is not None:
    print("key exist in dictionary")
else:
    print("given key is not exist in dictionary")
    