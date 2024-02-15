def rec(n):
    if n<=1:
        return n
    else:
        return n*rec(n-1)
n=int(input("Enter num: "))
f=rec(n)
print(f)