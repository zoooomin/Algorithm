#역수열(그리디)
n = int(input())
a = list(map(int,input().split()))
s = n-1
tmp = []
while s >= 0:
    tmp.insert(len(tmp)-a[s], n)
    s -= 1
    n -= 1
tmp.reverse()
print(tmp)