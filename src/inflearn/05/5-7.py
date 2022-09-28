#교육과정 설계
from collections import deque
a = input()
n = int(input())
cnt = 1
for x in range(n):
    plan = input()
    dq = deque(a)
    for i in plan:
        if i in dq:
            if i != dq.popleft():
                print(f'#{x + 1} NO')
                break

    else:
        if len(dq) == 0:
            print(f'#{x + 1} YES')
        else:
            print(f'#{x + 1} NO')

