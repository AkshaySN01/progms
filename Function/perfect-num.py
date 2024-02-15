def perfect(num):
    sum=0
    for i in range(1,num):
        if num%i==0:
            sum+=i
    if sum==num:
        print("perfect number")
    else:
        print("not perfect number")

n=int(input("Enter Number:"))
perfect(n)