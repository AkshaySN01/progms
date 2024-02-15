class Student:
    def __init__(self):
        self.name1='hi'
        self.p='tcr'
    def open(self):
        print(self.name1)
        print(self.p)

s1=Student()
print(s1.name1)
s1.name1='hello'
s1.open()