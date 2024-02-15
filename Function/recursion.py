def rec(n):
    if n<=1:
        return n
    else:
        return n+rec(n-1)
s=rec(5)
print(s)