n=int(input("Enter a number that you want to check:"))
flag=0
for i in range(n+1):
    if(i*(i+1)==n):
        flag=1
        break
if(flag==1):
    print(n,"is a pronic number")
else:
    print(n,"is not a pronic number")