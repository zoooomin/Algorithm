n, a = map(int, input().split())
n = list(map(int, str(n)))
stack = []
for x in n:
    while stack and a>0 and stack[-1]<x:
        stack.pop()
        a -= 1
    stack.append(x)

if a != 0:
    stack = stack[:-a]

# res = ''.join(map(str, stack))
for x in stack:
    print(x, end='')
