n=int(input("Enter the digit you want to print : "))
a=0
b=1
for i in range (1,n+1):
    c=a+b
    print(a)
    a=b
    b=c