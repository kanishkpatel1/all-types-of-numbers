n=int(input("Enter any number that you want to check : "))
num=n
sq=n**2
flag=0
t=10
while(n!=0):

    if(n%10!=sq%10):
        print("number is not automorphic ")
        flag=1
        break
    sq=sq//10
    n=n//10
if(flag==0):
        print(num," it is an automorphinc number : ")

