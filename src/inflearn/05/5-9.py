# Anagram(아나그램:구글 인터뷰 문제)
a = input()
b = input()
d = dict()
for i in a:
    d[i] = d.get(i, 0) + 1
for i in b:
    d[i] = d.get(i, 0) - 1

# if d1 == d2:
#     print("YES")
# else:
#     print("NO")

for x in a:
    if d.get(x) > 0:
        print("NO")
        break

else:
    print("YES")