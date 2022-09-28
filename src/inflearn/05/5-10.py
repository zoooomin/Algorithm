#최소힙
import heapq as hq
a = []
while True:
    n = int(input())
    if n == -1:
        break
    elif n == 0:
        if len(a) == 0:
            print(-1)
        else:
            print(hq.heappop(a)) #루트 노드 값을 pop
    else:
        hq.heappush(a, n)

