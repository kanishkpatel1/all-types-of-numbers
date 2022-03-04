import math
n=int(input("Enter the number that you want to check : "))
x=math.sqrt(n+1)
if int(x)==x:
    print(n,"is a sunny number")
else:
    print(n,"is not a sunny number ")
