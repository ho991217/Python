import sys
import heapq

heap = []

class MAXHEAP:
    def __init__(self):
        self.heap = []

    def process(self, cmd):
        if cmd == 0:
            if self.isEmpty():
                print(0)
            else:
                print(heapq.heappop(self.heap)[1])
        else:
            heapq.heappush(self.heap, (-cmd, cmd))

    def isEmpty(self):
        return self.heap == []

hp = MAXHEAP()
for _ in range(int(sys.stdin.readline())):
    hp.process(int(sys.stdin.readline()))