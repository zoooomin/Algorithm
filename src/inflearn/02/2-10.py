n = int(input())
a = list(map(int, input().split()))
s = 0
cnt = 0
for i in a:
    if i == 1:
        cnt = cnt + 1
        s += cnt
    else:
        cnt = 0
print(s)