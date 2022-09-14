from collections import deque
#침몰하는 타이타닉(그리디)
# n, m = map(int,input().split())
# a = list(map(int, input().split()))
# a.sort()
# cnt = 0
# while a:
#     if len(a) == 1: #한명이 남았을 때 처리방법
#         cnt += 1
#         break
#     if a[0] + a[-1] > m:
#         a.pop()
#         cnt += 1
#     else:
#         a.pop(0) #제일 가벼운 사람
#         a.pop()  # 제일 무거운 사람
#         cnt += 1
#
# print(cnt)

#deque로 구현하기
n, m = map(int,input().split())
a = list(map(int, input().split()))
a.sort()
a = deque(a)
cnt = 0
while a:
    if len(a) == 1: #한명이 남았을 때 처리방법
        cnt += 1
        break
    if a[0] + a[-1] > m:
        a.pop()
        cnt += 1
    else:
        a.popleft() #제일 가벼운 사람
        a.pop()  # 제일 무거운 사람
        cnt += 1

print(cnt)

