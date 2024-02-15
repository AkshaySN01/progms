def big(n):
    temp=num
    big=0
    while temp>0:
        digit=temp%10
        temp=temp//10
        if digit>big:
            big=digit
    print("Biggest digit is ",big)

num=int(input("Enter Number:"))
big(num)