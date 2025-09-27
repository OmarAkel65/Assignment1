# import math
# import sys
# import random
# from  enum import Enum
# print(math.pi)

# x = 0 
# for x in range(1,100):
#     if x %3 ==0 or x %5 == 0:
#         print(x)

def adder(x):
    def add(y):
        return x + y
    return add

add10 = adder(10)
print(add10(5))  # Should print 15
