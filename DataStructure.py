# 1. List - [] - ordered|mutable
# 2. tuple - () - ordered 
# 3. Dictionary - {} - unordered key: value pair x duplicates

'''mylist=[]
mylist=["Mike", "Acosta", "Esteron"]
mylist=["Mike", 90.50, "Emerson", 80.20, "Naniong", 80.20]

print(mylist[1])
print(mylist[:5])
print(mylist[::1])

mylist[0]="Michael"
mylist[:2]="James"

print(mylist)
mylist.append("berbon")
mylist.insert(0, "pico")

print(mylist)

mylist.pop()
mylist.pop(0)


print(mylist)

for x in mylist:
    print(f"{x}", end="")
print()
for x in range (len(mylist)):
    print(f"{mylist[x]}", end="")
print()

numbers=[9,7,6,8,4,5,2,1]

numbers.sort()
print(numbers)
print()

string=["b","c","a", "d"]
string.sort()
print(string)
print()

# mylist.reverse()
# print()
# print(mylist)

myList=[[1,4,10,2],[5,1,11,6]]

print(myList[0][2])

print()


for x in range(len(myList)):
    print(f"row {x+1}")
    myList[x].sort()
    myList[x].reverse()
    for y in range(len(myList[x])):
        print(myList[x][y], end=" ")
    print()


print()
print()'''

'''
list=[]
for x in range(5):
    print("Enter score : ")
    num = float(input())
    list.append(num)
'''

'''
col = int(input())
row = int(input())

myLest = [] 

for x in range(row):
    print(f"row {x+1}")
    print()
    
    for y in range(col):
        print(f"Enter Score {y}: \n " )
        num = float(input())
        myLest.append(num)
    

for a in range(len(myLest)):
    for b in range(len(myLest[a])):
        print(myLest[a][b], end=" ")
    print() nan'''

