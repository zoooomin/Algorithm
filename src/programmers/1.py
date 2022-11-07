# from itertools import permutations
# def solution(babbling):
#     answer = 0
#     babble = ['aya', 'ye', 'woo', 'ma']
#     wrd = []
#     for i in range(1, len(babble)+1):
#         for j in permutations(babble, i):
#             wrd.append(''.join(j))
#
#     for i in babbling:
#         if i in wrd:
#             answer += 1
#     return answer
def solution(babbling):
    answer = 0
    for b in babbling:
        for w in ['aya','ye','woo','ma']:
            if w*2 not in b:
                b = b.replace(w,'')
        if len(b.strip()) == 0:
            answer += 1
    return answer

babbling = ["ayaye", "uuuma", "ye", "yemawoo", "ayaa"]
a = solution(babbling)
print(a)