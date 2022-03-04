a=int(input("Enter the starting range : "))
b=int(input("Enter the end range : "))
for i in range(a,b):
    if(i%2==0):
        continue
    else:
        print(i)