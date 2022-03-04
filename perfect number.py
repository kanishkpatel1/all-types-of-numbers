n=int(input("Enter the number that you want to check : "))
sum=0
for i in range(1,n):
    if(n%i==0):
        sum=sum+i
if(sum==n):
    print("perfect number")
else:
    print("Not perfect number")
