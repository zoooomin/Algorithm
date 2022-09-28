#단어 찾기(해쉬)
n = int(input())
p = dict()
for i in range(n):
    wrd = input()
    p[wrd] = 1
for i in range(n-1):
    wrd = input()
    p[wrd] = 0

for key, val in p.items():
    if val == 1:
        print(key)
        break