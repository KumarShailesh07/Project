n = int(input("Enter the number of fibonacci series? : "))
f1 = 0 #first fibonacci number
f2 = 1 #second fibonacci number
c = 2 #show count

if n == 0:
    print(f1)
elif n == 1:
    print(f1, '\n' ,f2,sep="")
else:
    print(f1, '\n' ,f2 , sep="")
    while c < n:
        f = f1+f2
        print(f)
        f1,f2 = f2,f
        c+=1
        