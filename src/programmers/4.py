def solution(M, N):
    answer = 0
    if M == 1 and N == 1:
        answer = 0
    else:
        answer = M - 1 + M * (N-1)
    return answer

print(solution(2,2)) #m:가로 n:세로
print(solution(2,5))
print(solution(3,3))