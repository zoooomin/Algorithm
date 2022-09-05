def solution(info, query):
    answer = []
    c = list()
    for x in info:
        cnt = 0
        x = x.split(' ')
        print(x)
        for i in query:
            i = i.split(' and ')
            i = i[:3] + i[-1].split(' ')
            i = list(set(i))
            if '-' in i:
                i.remove('-')
            print(i)
            l = len(set(i)-set(x))
            if l == 0:
                cnt += 1

    # return answer


info = ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
query = ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]
solution(info, query)
