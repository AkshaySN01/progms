class Customer:
    def __init__(self,name,acc_no):
       self.name=name
       self.acc_no=acc_no
       self.amt=0
    def opt1(self,d):
        self.amt+=d
        print("Deposited")
        print('Balance=',self.amt)
    def opt2(self,w):
        if w<self.amt:
            self.amt-=w
            print("Withdrawn ",w)
            print("Balance=",self.amt)
        else:
            print('Insufficient Balance')
    def opt3(self):
        print("Balance=",self.amt)

n=input('Enter the name of customer: ')
a=input('Enter the account number of customer: ')
cust=Customer(n,a)
print('ACCOUNT DETAILS \n _______________ \n Account Holder= ',cust.name,'\n Account Number= ',cust.acc_no)
c=3
while c!=4:
  print("\n1.Deposit Money \n 2.Withdraw Money \n 3.View Balance \n 4.Exit")
  c=int(input())
  if c==1:
      deposit=int(input('Enter deposit amount: '))
      cust.opt1(deposit)
  elif c==2:
      withdraw=int(input('Enter withdraw amount: '))
      cust.opt2(withdraw)
  elif c==3:
      cust.opt3()
if c==4:
    exit