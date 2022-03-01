import sys
import heapq

T = int(sys.stdin.readline())

for _ in range(T):
    k = int(sys.stdin.readline())
    maxHeap = []
    minHeap = []
    checked = [False] * k

    for i in range(k):
        cmd, number = sys.stdin.readline().rstrip().split()

        if cmd == 'I':
            heapq.heappush(maxHeap, (-int(number), i))
            heapq.heappush(minHeap,(int(number), i))
            checked[i] = True

        else:
            if number == "1":
                while maxHeap and checked[maxHeap[0][1]] is False:
                    heapq.heappop(maxHeap)

                if maxHeap:
                    checked[maxHeap[0][1]] = False
                    heapq.heappop(maxHeap)

            else:
                while minHeap and checked[minHeap[0][1]] is False:
                    heapq.heappop(minHeap)

                if minHeap:
                    checked[minHeap[0][1]] = False
                    heapq.heappop(minHeap)


    if True not in checked:
        print('EMPTY')
    else:
        while maxHeap and checked[maxHeap[0][1]] == False:
            heapq.heappop(maxHeap)
        while minHeap and checked[minHeap[0][1]] == False:
            heapq.heappop(minHeap)

        print(-maxHeap[0][0], minHeap[0][0])
