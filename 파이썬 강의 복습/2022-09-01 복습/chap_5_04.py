# 성적이 90점 이상:A, 80점 이상:B, 70점 이상:C, 60점 이상:D, 그 외에는 F를 반환하는 함수 getGrade(score)를 작성하고 테스트 하라.

def getGrade(score):
    if score >= 90:
        Grade = 'A'
    elif score >= 80:
        Grade = 'B'
    elif score >= 70:
        Grade = 'C'
    elif score >= 60:
        Grade = 'D'
    else:
        Grade = 'F'
    return Grade

x = int(input("점수를 입력하세요: "))

print("성적은",getGrade(x),"입니다.")