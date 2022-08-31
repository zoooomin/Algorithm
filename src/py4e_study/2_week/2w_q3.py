#Q3. 학생 이름과 점수를 입력하면 학점을 출력하는 학점 변환기
def grader(name, score):
    if score >= 95:
        grade = 'A+'
    elif score >= 90:
        grade = 'A'
    elif score >= 85:
        grade = 'B+'
    elif score >= 80:
        grade = 'B'
    elif score >=75:
        grade = 'C+'
    elif score >= 70:
        grade = 'C'
    elif score >= 65:
        grade = 'D+'
    elif score >= 60:
        grade = 'D'
    else:
        grade = 'F'
    print('학생 이름 : ',name)
    print('점수 : %i점'%score)
    print('학점 : ',grade)

name = input('학생 이름을 입력해 주세요: ')
score = int(input('점수를 입력해 주세요: '))
grader(name, score)