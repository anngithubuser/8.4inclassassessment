"""
OrderOfNumbers
"""
# Provide your solution here

n1= int(input("Please write n1: "))
n2= int(input("Please write n2: "))
n3= int(input("Please write n3: "))

if n1<n2 and n2<n3:
    input("numbers are ascending")
elif n1>n2 and n2>n3:
    input("numbers are descending")
else:
    if (n1%2)==0 and (n2%2)==0 and (n3%2)==0:
        input("no specific order, but all even")
    elif (n1%2)==1 and (n2%2)==1 and (n3%2)==1:
        input("no specific order, but all odd")
    else:
        input("no specific order")


"""
SumUp
"""
# Provide your solution here
n1= int(input("Please write 1st number: "))
n2= int(input("Please write 2nd number: "))

print(list(range(n1,n2)))

if n1>n2:
    input("n2 needs to be > n1")
elif n1<0 or n2<0:
    input("n1 and n2 need to be > 0")
