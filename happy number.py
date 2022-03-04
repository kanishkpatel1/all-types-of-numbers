n=int(input("Enter the number that you want to check :"))
temp=n
sum=0
while(sum!=1 and sum!=4):
    sum=0
    while(n!=0):
        rem=n%10
        sum+=rem**2
        n=n//10
    n=sum
if(sum==1):
    print(temp,"is a Happy number")
else:
    print(temp,"is Unhappy number")