word=input("Enter a word: ")
n=len(word)
pal=""
for i in range(0,n):
    c=word[n-1]
    pal+=c
    n-=1
if word==pal:
    print("palindrom")
else:
    print("not palindrom")
