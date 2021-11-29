class Student:
    name = ""
    java = 0
    c = 0
    stot = 0
    savg = 0

    def __init__(self, name, java, c):
        self.name = name
        self.java = java
        self.c = c

    def tot(self):
        self.stot = self.java + self.c
        return self.stot

    def avg(self):
        self.savg = self.stot / 2

    def disp(self):
        self.tot()
        self.avg()
        print(self.name, self.java, self.c, self.stot, self.savg, sep="\t")


class StudentEx(Student):
    python = 0

    def __init__(self, name, java, c, python):
        super().__init__(name, java, c)
        self.python = python
        self.tot()
        self.avg()

    def tot(self):
        self.stot = super().tot() + self.python

    def avg(self):
        self.savg = self.stot / 3

    def disp(self):
        print(self.name, self.java, self.c, self.python, self.stot, self.savg, sep="\t")


s1 = StudentEx("엑스맨", 80, 85, 78)
s2 = StudentEx("배트맨", 90, 85, 75)
s3 = StudentEx("슈퍼맨", 100, 20, 45)

s1.disp()
s2.disp()
s3.disp()