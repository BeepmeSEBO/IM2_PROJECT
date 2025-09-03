# #generate random numbers, guess what number if wrong, number of tries will increment, if guessed right print correct
# import random
# nam = random.randint(0, 10)
# tries = 0
# while(True):
#     print("Guess the number from 0 to 10: ")
#     guess = int(input())
    
#     if nam == guess:
#         print(f"{tries} tries bago ka tama")
#         break
#     elif tries == 3:
#         print("TAMA KANA GAGO PATAY KANA")
#         print()
#         break
#     elif guess>10:
#         tries +=1
#         print("ANLAKI")
#         print("Enter Number from 1-10")
#         print()
#     elif guess<0:
#         tries +=1
#         print("LIIT")
#         print(" 1-10 NGANI")
#         print()
#     elif nam>guess:
#         tries +=1
#         print("HEL LOW")
#         print()
#     elif nam<guess:
#         tries +=1
#         print("Naka HIGH")
#         print()
#     else:
#         tries +=1
#         print("NOT A NUMBER")
#         print("1 TO 10 NGANI")
#         print()

#_______________________________________
# print("enter")
# star=int(input())
#_______________________________________
# *
# * *
# * * *
# * * * * 

# for a in range(star, 0, -1):
#     for b in range(a, star):
#         print(f"*", end=" ")
#     print()

# * * * *
# * * *
# * * 
# *

# for a in range(0, star, 1):
#     for b in range(a,star):
#         print(f"*", end=" ")
#     print()

# * * * *
#  * * *
#   * *
#    *

# for x in range(star, 0, -1):

#     for spes in range(star-x):
#         print(" ", end='')

#     for yehyeh in range(x):
#         print("*", end=' ')

#     print()

#     *
#    * *
#   * * * 
#  * * * * 

# for x in range(star, 0, -1):

#     for spes in range(x):
#         print(" ", end='')

#     for yehyeh in range(star-x):
#         print("*", end=' ')

#     print()

# * * * * 
#   * * *
#     * *
#       *

# for a in range(star, 0, -1):
#     for space in range(star - a):
#         print(" ", end=" ")

#     for b in range(a):
#             print("*", end=" ")
#     print()

#       * 
#     * *
#   * * *
# * * * *

# for a in range(star, 0, -1):
#     for space in range(a):
#         print(" ", end=" ")

#     for b in range(star-a):
#             print("*", end=" ")
#     print()
print("EnterNAME: ")
name = input()

# for t in range(1,5)
#     for T in range(1,5)
#         print(T)

print(name[::-1])