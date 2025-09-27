def hello():
    print("Hello")

hello()

def sum(num1,num2):
    print(num1 + num2)

sum(2,3)

def summ(nums1=0,nums2=0):
    if (type(nums1) is not int or type(nums2) is not int):
        return 0
    return nums1 + nums2
total = summ(1,4)
print(total)

def multiple_items(*args):
    print(args)
    print(type(args))

multiple_items("dave","john","sara")

def multiple_named_items(**kwargs):
    print(kwargs)
    print(type(kwargs))

multiple_named_items(First = "dave",Last = "john")

i=7
def multiplication (m,n):
    
    if m % i == 0 or n % i ==0 :
        print("nice")
    else:
        print(n+m)
multiplication(1,0)

def people(*person): # * take how many arg you give
    for i in person:
        print(f"Hello {i}")
people("Omar","Ahmad")

def show_details(name,*skills):
    print(f"{name} your skills is:")
    for skill in skills:
        print(skill)

show_details("Omar", "Baseball", "Football", "swimming")
show_details("Ahmad", "Baseball", "Football", "swimming")
