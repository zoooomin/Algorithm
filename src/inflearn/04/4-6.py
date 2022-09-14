#씨름 선수 (그리디 알고리즘)
n = int(input())
l = []
for i in range(n):
    h, w = map(int, input().split())
    l.append((h, w))
l.sort(reverse=True)
largest = 0
cnt = 0
for h, w in l:
    if w > largest:
        largest = w
        cnt += 1

print(cnt)