#회의실 배정(그리디)
#회의가 끝나는 시간을 기준으로 정렬
'''
회의를 최대한 많이 해야하기 때문에
회의가 끝나는 시간이 빨라야 됨
'''
#1. 배열로 접근하는 방법
#2. 튜플로 접근하는 방법
#1
# n = int(input())
# l = []
# for _ in range(n):
#     a, b = map(int, input().split())
#     l.append([a, b])
# ###############
# l.sort(key=lambda x:(x[1],x[0]))
#
# cnt = 1
# s = l[0][1]
#
# for x in l:
#     if x[0] >= s:
#         cnt += 1
#         s = x[1]
# print(cnt)
#2
n = int(input())
l = []
for i in range(n):
    s, e = map(int, input().split())
    l.append((s, e))
l.sort(key=lambda x:(x[1], x[0]))
cnt = 0
ep = 0
for s, e in l:
    if s >= ep:
        ep = e
        cnt += 1
print(cnt)