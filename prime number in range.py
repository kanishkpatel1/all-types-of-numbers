start=int(input("Enter the starting no : "))
end=int(input("Enter the ending no : "))
count=0
for i in range(start,end+1):
    count=0
    for j in range(1,i+1):
        if(i%j==0):
            count=count+1
    if count==2:
        print(i)