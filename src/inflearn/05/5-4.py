#후위식 연산
a = input()
stack = []
ans = 0
for x in a:
    if x.isdecimal():
        stack.append(int(x))
    else:
        if x == '+':
            ans = stack.pop(-2) + stack.pop()
            stack.append(ans)
        elif x == '-':
            ans = stack.pop(-2) - stack.pop()
            stack.append(ans)
        elif x == '*':
            ans = stack.pop(-2) * stack.pop()
            stack.append(ans)
        elif x == '/':
            ans = stack.pop(-2) / stack.pop()
            stack.append(ans)
print(stack.pop())