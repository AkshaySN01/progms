class att:
   def __init__(self):
      self.name=""
      self.code=0
      self.b_sal=0.0
      self.dept=""
      self.no_stud=0
      self.a=[]

   
   def roll(self):
      print("Enter the attendance roll number wise(1-present/0-absent):")
      for i in range(self.no_stud):
         s=int(input())
         self.a.append(s)

   def input(self):
      self.name=input("Enter name of teacher: ")
      self.code=input("Enter code of teacher: ")
      self.b_sal=int(input("Enter basic salary of teacher: "))
      self.dept=input("Enter department of the teacher: ")
      self.no_stud=int(input("Enter number of students: "))
      self.roll()
      print("__________________________________________\n")


   def display(self):
      print("Name: ",self.name)
      print("Empcode: ",self.code)
      print("Department: ",self.dept)
      print("Basic Salary: ",self.b_sal)
      print("list of absent students:")
      l=len(self.a)
      for i in range(l):
         if self.a[i]==0:
           print(i+1)
      print("list of present students:")
      for i in range(l):
         if self.a[i]==1:
           print(i+1)
      print("__________________________________________\n")

num=int(input("Enter number of teachers: "))
L=[]
for i in range(num):
  obj=att()
  obj.input()
  L.append(obj)
for i in range(num):
  L[i].display()
