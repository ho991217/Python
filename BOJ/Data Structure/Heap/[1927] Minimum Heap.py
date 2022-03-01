import sys
import heapq

heap = []

class MINHEAP:
    def __init__(self):
        self.heap = []

    def process(self, cmd):
        if cmd == 0:
            if self.isEmpty():
                print(0)
            else:
                print(heapq.heappop(self.heap))
        else:
            heapq.heappush(self.heap, cmd)

    def isEmpty(self):
        return self.heap == []

hp = MINHEAP()
for _ in range(int(sys.stdin.readline())):
    hp.process(int(sys.stdin.readline()))