# user = int(input("Enter how many number: "))

# list = []

# for i in range(user):
#     list.append(int(input(f"Enter num {i + 1}: " )))

# print(list)

# lists = tuple(list)

# search = int(input("Search Number: "))

# print(list.index(search))
# print(list.count(search))

# print()


new = int(input("Enter how many: "))

dictionary = {}

for a in range(new):
    name = input(f"Enter Name for person {a+1}: ")
    dictionary[name] = {}
    
    sub = int(input("Enter how many subjects: "))

    for b in range(sub):
        subject = input(f"Enter subject for {name}: ")
        gred = int(input(f"Enter grade for their subject in {subject}: "))
        dictionary[name][subject] = gred

print(f"Your dict: {dictionary}")
print(dictionary.keys())
print(dictionary.keys())

print(dictionary.values())
print(dictionary.items())

