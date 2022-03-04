n=int(input("Enter a number: "))
num=n
count=0
while n!=0:
    if(n%2==1):
        count+=1
    n=n//2
if(count%2==0):
    print(num,"is a Evil Number")
else:
    print(num,"is not  a Evil Number")