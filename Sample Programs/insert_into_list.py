lim=int(input("Enter Limit: "))
li=[]
for i in range(lim):
    a=int(input('Enter Element '+str(i+1)+": "))
    li.append(a)
print(li)
li.insert(2,"inserted")
print(li)
