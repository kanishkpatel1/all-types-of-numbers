a=int(input("Enter a number that you want to check\n"))
b=0
for i in range(1,a+1):
    if(a%i==0):
        b=b+1
    
if(b==2):
    print("Number is   prime\n")
else:
    print("The number is not prime\n")