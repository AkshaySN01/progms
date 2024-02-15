class grade:
    n=0
    def calc(self):
        s=float(input())
        self.n+=s

    def disp(self):
        self.avg=self.n/5
        print("Average score=",self.avg)

    def grade(self):
        if self.avg>90:
            grd='A'
        elif self.avg<90 and self.avg>75:
            grd='B'
        elif self.avg<75 and self.avg>55:
            grd='C'
        else:
            grd='F'
        print('Grade=',grd)


obj=grade()
stud=input("Student: ")
print("Marks in 5 Subjects: ")
for i in range(5):
    obj.calc()
obj.disp()
obj.grade()