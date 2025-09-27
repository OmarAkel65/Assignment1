#Dictionaries
band = {
    "vocal" : "plant",
    "guitar" : "page"
}
band2 = dict(vocal = "plant" , guitar= "page" )

print(band)
print(band2)
print(type(band))
print(len(band2))

#Access items
print(band["vocal"])
print(band.keys())

#list all items
print(band.values())

#list of keys/values pairs as tuples
print(band.items())

#verify key exists
print("guitar" in band)

#change values
band["vocal"] ="coverdale"
band.update({"bass" : "jpj"})
print(band)

#remove items
print(band.pop("bass"))
print(band)

band["drums"] = "omar"
print(band)

print(band.popitem()) #tup
print(band)

# delete and clear
band["drums"] = "omar"
del band["drums"]
print(band)

band2.clear()
print(band2)

# del band

# copy dictionaries
# band2 = band # create a reference
# print("bad copy")
# print(band2)
# print(band)

# band2["drums"] = "ahmad"
# print(band)

band2 = band.copy()
band2 ["drums"] = "omar"
print("good copy")
print(band)
print(band2)

# or use the  dict()
band3 = dict(band)
print("good copy")
print(band3)

#nested dictionaries
member1 = {
    "name" : "plant",
    "instrument" : "vocals"
}

members2 = {
    "name" : "page",
    "instrument" : "guitar"
}
band = {
    "member1" : member1,
    "member2" : members2
}
print(band)
print(band["member1"]["name"])

#sets

nums = {1,2,3,4}
nums2 = set((1,2,3,4))
print(nums)
print(nums2)
print(type(nums))
print(len(nums))

#no duplicate allowed
nums = {1,2,2,3,3,4}
print(nums)

#true is a dupe of 1, false is dupeof zero

nums = {1,True,2,False,2,3,4,0}
print(nums)
#check if a value is in a set
print(2 in nums)

#but you canot refer to an element on the set with an index position or a key

#add a new element to a set 
nums.add (9)
print(nums)

#add elements from one set to another
morenums = {5,6,7}
nums.update(morenums)
print(nums)
#you can use update with lists , tuples,and dictionaries too

#merge two sets to create a new set
one = {1,2,3}
two = {5,6,7}

mynewset = one.union(two)
print(mynewset)

#keep only the duplicate
one = {1,2,3}
two = {2,3,4}
one.intersection_update(two)
print(one)

#keep everything except the duplicate
one = {1,2,3}
two = {2,3,4}

one.symmetric_difference_update(two)
print(one)








