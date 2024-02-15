
num=int(input("Enter Number:"))
a=num
sum=0
while a>0:
    digit=a%10
    a//=10
    sum+=digit*digit*digit
print(sum)
if sum==num:
    print("Armstrong")
else:
    print("Not Armstrong number")
