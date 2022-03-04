ch=65
n=int(input("Enter the numver : "))
for i in range(n+1):
    for k in range(i):
        print(" ",end="")
    for j in range(i):
        print(chr(ch),end=" ")
        ch=ch+1
    print("\r")