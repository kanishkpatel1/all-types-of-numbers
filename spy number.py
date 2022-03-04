sum=0
product=1
n=int(input("Enter any number that you want to check : "))
while(n!=0):
    rem=n%10
    sum+=rem
    product*=rem
    n=n//10
if(sum==product):
    print("Number is spy!")
else:
    print("Number is not spy! ")