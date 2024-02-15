num=int(input("Enter Number:"))
A=0
for i in range(2,num):
    if num%i==0:
        A=1
        break
if A==0:
    print("Prime Number")
else:
    print("not Prime Number")
    