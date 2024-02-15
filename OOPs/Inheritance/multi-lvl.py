class Student():
    def p1(self):
        print('open')
    
class Teacher(Student):
    def p2(self):
        print('closed')

class School(Teacher):
    def c(self):
        print('parent')

obj=School()
obj.p1()
obj.p2()
obj.c()