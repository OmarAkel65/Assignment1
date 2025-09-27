users = ["omar", "ahmad", "bob"]
data = ["dave", "43" , "true"]
emptylist =[]
print("dave " in emptylist)
print(users[0])
print(users[-2:])
print(users.index("omar"))
print(users[0:2])
print(users[1:])
print(users[-3:-1])
print(len(data))

users.append("elsa")
print(users)

users.extend(data)
print(users)

users[2:2] = ["eddie" , "alex"]
print(users)

users[1:3] = ["robbert" , "jb"]
print(users)

users.remove("robbert")
print(users)


print(users.pop())
print(users)

data.clear()
print(data)

users.insert(0 , "ali ")
print(users)

users[1:2] = ["omar"]
users.sort()
print(users)

users.sort(key = str.lower)
print(users)

nums = [5,1,70,50,60,55]
nums.reverse()
print(nums)

nums.sort(reverse = True)
print(nums)

print(sorted(nums, reverse = True))
print(nums)

numscopy = nums.copy()
mynums = list(nums)
mycopy = nums[:]

print(numscopy)
print(mynums)
mycopy.sort()
print(mycopy)
print(nums)

mylist = list([1, "omar" , True])
print(mylist)

# tuple

mytuple = tuple(("ahmad" ,45,"you"))
anothertuple = tuple(("you" ,"are" ,"ok"))
print(mytuple)
print(type(mytuple))

newlist = list(mytuple)
newlist.append("adam")
newtuple = tuple(newlist)
print(newlist)

(one , two , *hey) = anothertuple 
print(one)
print(two)
print(hey)





