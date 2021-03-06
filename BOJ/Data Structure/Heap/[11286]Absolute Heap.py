import sys
import heapq

N = int(sys.stdin.readline())
# heap = []
# check = dict()
#
# for _ in range(N):
#     cmd = int(sys.stdin.readline())
#
#     if cmd == 0:
#         if heap == []:
#             print(0)
#         else:
#             minAbs = heap[0]
#             if check[minAbs][0] >= 1:
#                 check[minAbs][0] -= 1
#                 print(-minAbs)
#             elif check[minAbs][1] >= 1:
#                 check[minAbs][1] -= 1
#                 print(minAbs)
#             if check[minAbs] == [0, 0]:
#                 heapq.heappop(heap)
#
#     else:
#         absol = abs(cmd)
#         if absol in heap:
#             if cmd > 0:
#                 check[absol][1] += 1
#             else:
#                 check[absol][0] += 1
#         else:
#             heapq.heappush(heap, absol)
#             if cmd > 0:
#                 check[absol] = [0, 1]
#             else:
#                 check[absol] = [1, 0]
minusHeap = []
plusHeap = []

for _ in range(N):
    cmd = int(sys.stdin.readline())

    if cmd == 0:
        if minusHeap and plusHeap:
            if minusHeap[0] <= plusHeap[0]:
                print(-heapq.heappop(minusHeap))
            else:
                print(heapq.heappop(plusHeap))

        elif not minusHeap and plusHeap:
            print(heapq.heappop(plusHeap))

        elif not plusHeap and minusHeap:
            print(-heapq.heappop(minusHeap))

        else:
            print(0)

    elif cmd < 0:
        heapq.heappush(minusHeap, -cmd)

    else:
        heapq.heappush(plusHeap, cmd)
