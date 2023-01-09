c = int(input())
for _ in range(c):
    n = list(map(int, input().split()))
    cnt = 0
    tot = sum(n) - n[0]
    avg = tot/n[0]
    for i in range(1, n[0]+1):
        if n[i] > avg:
            cnt += 1
    ans = (cnt / n[0]) * 100
    print(f'{ans:.3f}%')