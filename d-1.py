#name=input("Enter the name:")
#print(f"name:{name}")
#print (5**2)
a = 2
b = 5
c = 10

# Using other names to avoid overwriting built-ins
maximum = ""
minimum = ""

if a >= b and a >= c:
    maximum = a
    minimum =a
    print("a is larger than b & c")
    print("a is lower")
elif b >= a and b >= c:
    maximum = b
    print("b is larger than a & c")
else:
    maximum = c
    print("c is larger than a & b")
    print ("a is lower")