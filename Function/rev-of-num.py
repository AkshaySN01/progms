def rev(n):
    r=0
    while n!=0:
        a=n%10
        n=n//10
        r=(r*10)+a
    return r
num=int(input('Enter num: '))
print(rev(num))