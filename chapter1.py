# x = int(input("enter value of x: "))
# if x > 0:
#     print("x is positive")
# elif x < 0:
#     print("x is negative") 
# else:
#     print("x is zero")

# import string
# letters = string.ascii_lowercase
# for first in letters:
#     for second in letters:
#         if first == second:
#             continue
#         print(first + second)

for x in range(0,5):
    for y in range(0, x + 1):
        print("*" , end="")
    print()
    