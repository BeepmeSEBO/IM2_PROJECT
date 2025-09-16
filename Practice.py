'''str="Mike Acosta"
print(str[::])
print(str[2::])
print(str[::-1])
print(str[1:7:2])
print(str[-6:-1:2])
print(str[-6:-10:-2])

for x in range(1,11):
    for y in range(10,x-1,-1):
        print(f"{y}", end=" ")
    print()

for a in range(1, 6):
    for b in range(6,11):
        print(f"{a}{b}", end=" ")
    print()
'''
'''print("Enter matrix size: ")
number = input()'''

'''#while loop
while(True):
    print("Enter number: ")
    z=int(input())
    if z<=0:
        break'''



print("Enter string: ")
stri=input().upper()
       
for z in stri:
    print(z)

for z in range(len(stri)):
    print(stri[z])

