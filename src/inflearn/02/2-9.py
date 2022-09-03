n = int(input())
money = 0
res = 0
for i in range(n):
    tmp = list(map(int, input().split()))
    tmp.sort()

    a, b, c = map(int, tmp)

    if (a == b) & (b == c):
        money = 10000 + a * 1000
    elif (a == b) or (a == c):
        money = 1000 + a * 100
    elif b == c:
        money = 1000 + b * 100
    else:
        money = c * 100

    if money > res:
        res = money

print(res)