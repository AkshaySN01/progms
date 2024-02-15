def amstr(n):
    a=num
    sum=0
    while a>0:
        digit=a%10
        a//=10
        sum+=digit*digit*digit
    if sum==num:
        print("Armstrong")
    else:
        print("Not Armstrong number")

num=int(input("Enter Number:"))
amstr(num)