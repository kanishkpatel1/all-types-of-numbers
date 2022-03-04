start=int(input("Enter starting range : "))
end=int(input("Enter ending range : "))
for i in range(start,end+1):
    fact=1
    cn=i
    for j in range(1,i+1):
        fact=fact*j
    print(cn,"!=",fact)