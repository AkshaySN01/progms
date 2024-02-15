class Parent():
    def s(self):
        print('parent')

class Child(Parent):
    def c(self):
        print('child')

obj=Child()
obj.s()
obj.c()