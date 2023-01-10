n = [0] * 10001

for i in range(1, 10001):
    if n[i] == 0:
        while i < 10001:
            i = sum(list(map(int, str(i)))) + i
            if i < 10001:
                n[i] = 1

for i in range(1, 10001):
    if n[i] == 0:
        print(i)
