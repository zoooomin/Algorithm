# 학생 답
s = ["김갑,3242524215",
"이을,3242524223",
"박병,2242554131",
"최정,4245242315",
"정무,3242524315"]

# 정답지
a = [3,2,4,2,5,2,4,3,1,2]

def grader(s,a):
    std_grade = []
    for std in s:
        t = 0
        wrg_ans = 0

        std_ans = std.split(",")[1] #이름과 답을 분리하여 답만 따로 정답지와 비교
        std_ans = list(map(int, std_ans))
        for ans_num in a:
            if ans_num != std_ans[t]:
                wrg_ans += 1 #정답지가 비교하여 틀린 갯수 체크
            t += 1
        score = 100 - 10 * wrg_ans #점수 계산
        slist = []
        slist.append(std.split(",")[0])
        slist.append(score)
        std_grade.append(slist) #2차원 배열 생성 : [[이름,성적],[이름,성적]....]

    std_grade.sort(key = lambda x:x[1], reverse=True) #lambda를 사용하여 성적별 배열 정리

    i = 1
    for name, grade in std_grade:
        print(f'학생: {name} 점수: {grade} {i}등')
        i += 1 #등수 표시 변수

grader(s, a)