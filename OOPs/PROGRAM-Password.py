class Choice:
    def __init__(self,p):
        self.p=p
    def login(self):
        pa=input('Enter Password')
        if self.p!=pa:
            print("Invalid Password!!!")
        else:
            print("Logged in!!")
    def reset(self):
        new=input("Enter new password: ")
        self.p=new
        print("Password changed!!")
        
p=input('Enter a password: ')
obj=Choice(p)
c=1
while(c!=3):
    print("1.Login \n2.Reset Password \n3.Exit")
    c=int(input('Enter your choice: '))
    if c==1:
        obj.login()
    elif c==2:
        obj.reset()
    elif c==3:
        exit
    else:
        print("Invalid")