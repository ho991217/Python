# 오버라이딩

class Course:
    name = "이름"
    java = 0
    c = 0
    ple = 0
    avg = 0

    def __init__(self, name, java, c):
        self.name = name
        self.java = java
        self.c = c
        self.ple = java + c
        self.avg = self.ple / 2

    def Show(self):
        print(self.name, self.java, self.c, self.sum, self.avg, sep = "\t\t")

    def retSum(self):
        return self.ple


class StudentEx(Course):
    python = 0
    ple = 0
    avg = 0

    def __init__(self, name, java, c, python):
        super().__init__(name, java, c)
        self.python = python
        self.ple = java + c + python
        self.avg = self.ple / 3

    def Show(self):
        print(self.name, self.java, self.c,self.python, self.ple, self.avg, sep = "\t\t")

s1 = StudentEx("엑스맨", 80, 85, 90)
s2 = StudentEx("배트맨", 90, 85, 80)
s3 = StudentEx("슈퍼맨", 100, 20, 25)

s1.Show()
s2.Show()
s3.Show()