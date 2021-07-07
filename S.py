def F(p):
    if p< 0:
        print("invalid Input")
    elif p==0 :
        return 0
    elif p==1 or p==2:
        return 1
    else :
        return F(p-1)+F(p-2)
n=int(input("Enter the value of n: "))
print("the febonacci series is : ",end = ' ')
for n in range(0,n):
    print(F(n), end = ' ')



