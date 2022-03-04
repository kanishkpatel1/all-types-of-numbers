n=int(input("Enter the number that you want to check : "))
num=n
cube=n**3
flag=1
while n!=0:
    if(n%10!=cube%10):
        flag=0
        break
    n=n//10
    cube=cube//10
if(flag==1):
    print(num,"is a trimorphic number")
else:
    print(num,"is not a trimorphic number")
