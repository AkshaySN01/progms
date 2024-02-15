#create file exclusively
#f=open("text.txt",'x')
#f.write("hello")
#f.close()

#write
f=open("text.txt",'w')
f.write('hi python')
f.close()

#append
f=open("text.txt",'a')
f.write('''
Hello
python''')
f.close()

#read
f=open("text.txt",'r')
print(f.read())
f.close()

#readline
f=open("text.txt",'r')
print(f.readline())
f.close()

#readlines
f=open("text.txt",'r')
print(f.readlines())
f.close()