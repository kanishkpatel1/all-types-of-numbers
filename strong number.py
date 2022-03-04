n=int(input("Enter the number that you want to check"))
temp=n
sum=0
while(n!=0):
    r=n%10
    fact=1
    for i in range(1,r+1):
        fact=fact*i
    sum+=fact
    n=n//10

if(temp==sum):
    print("Number is strong")
else:
    print("Number is not strong")