#쇠막대 자르기
a = input()
stack = []
s = 0
for i in range(len(a)):
    if a[i] == '(':
        stack.append(a[i])
    else:
        stack.pop()
        if a[i-1] == '(':
            s += len(stack)
        else:
            s += 1
print(s)