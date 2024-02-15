n=int(input("limit: "))
"""
for i in range(n):
    for j in range(i+1):
        print("*",end="")
    print()
"""
"""
for i in range(n,0,-1):
    for j in range(i):
        print("*",end="")
    print()
"""

temp=0
for i in range(n,0,-1):
    temp+=1
    for j in range(i):
        print(temp,end="")
    print()

"""
for i in range(1,n+1):
    for j in range(i):
        print(i,end="")
    print()
"""
"""
for i in range(n+1):
    for j in range(1,i+1):
        print(j,end="")
    print()
"""