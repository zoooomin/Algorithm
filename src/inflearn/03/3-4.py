#두 리스트 합치기(옳지 않은 풀이 -> 데이터가 커질 수록 시간이 오래 걸리기 때문이다.)
# n = int(input())
# x = list(map(int,input().split()))
# m = int(input())
# y = list(map(int, input().split()))
# l = x + y
# l.sort()
# print(l)
# 강사님 풀이
n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))
c = list()
i, j = 0, 0
while i<n and j<m:
    if a[i] <= b[j]:
        c.append(a[i])
        i += 1
    else:
        c.append(b[j])
        j += 1
if i<n:
    c += a[i:]
elif j<m:
    c += b[j:]

for x in c:
    print(x,end=' ')