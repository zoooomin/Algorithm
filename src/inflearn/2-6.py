#자릿수의 합
n = int(input())
x = list(map(int, input().split()))

def digit_sum(a):
    sum = 0
    for i in str(a):
        sum += int(i)
    return sum

max = -214700000
for a in x:
    tot = digit_sum(a)
    if tot > max:
        max = tot
        res = a

print(res)
