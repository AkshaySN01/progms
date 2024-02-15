limit=int(input("Enter Number of items:"))
arr=[]
big=0
for i in range (0,limit):
    num=int(input("Enter Number"+str(i+1)+" : "))
    arr.append(num)
for i in range (0,limit):
    if arr[i]>big:
        big=arr[i]
print("Biggest is ",big)
