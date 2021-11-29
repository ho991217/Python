class Clock:
    def __init__(self, hour, min):
        self.hour = hour
        self.min = min

    def solution(self):
        c = self.min - 45
        if c >= 0: self.min = c
        else:
            self.hour -= 1
            self.min = 60 + c
            if self.hour < 0:
                self.hour += 24

        print(self.hour,self.min)

            

h, m = map(int, input().split(' '))
clock = Clock(h, m)
clock.solution()




