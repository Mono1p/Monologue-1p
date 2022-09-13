#학생의 작문 리포트를 입력으로 받아서 중복되지 않은 단어가 많으면 점수를 높게 매기는 프로그램으로 변경해보자. 
#예를 들어, 중복되지 않은 단어의 개수가 전체 단어 개수의 50%가 넘으면 학점 A를 부여한다.

report = input("작문 리포트를 입력하시오 : ")

words = report.split(" ")

test = set(words)

result = len(words) - len(test)

if result <= len(words) * 0.5 :
    grade = 'A'
elif result <= len(words) * 0.6 :
    grade = 'B'
elif result <= len(words) * 0.7 :
    grade = 'c'
elif result <= len(words) * 0.8 :
    grade = 'D'
else:
    grade = 'F'
print(f"전체 단어 : {len(words)}, 중복되지 않은 단어 : {len(test)}, 학점 : {grade}")