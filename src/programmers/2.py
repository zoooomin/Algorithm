def solution(common):
    answer = 0
    cha = 0
    gob = 0
    if (common[2] - common[1]) == (common[1] - common[0]):
        cha = common[1] - common[0]
        answer = common[-1] + cha
    else:
        gob = common[1]//common[0]
        answer = common[-1] * gob

    return answer

# common = [1,2,3,4]
common = [2,4,8]
print(solution(common))