#창고 정리
l = int(input())
a = list(map(int, input().split()))
m = int(input())
a.sort()
while m>0:
    m -= 1
    a[0] += 1 #가장 낮은 곳
    a[-1] -= 1 #가장 높은 곳
    a.sort()

print(a[-1]-a[0])