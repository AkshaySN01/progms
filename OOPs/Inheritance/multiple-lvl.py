class Student():
    def p1(self):
        print('open')

class Teacher():
    def p2(self):
        print('closed')

class Child(Student,Teacher):
    def c(self):
        print('welcome')

obj=Child()
obj.p1()
obj.p2()
obj.c()