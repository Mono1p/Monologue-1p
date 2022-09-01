# 다음 리스트에 저장된 정수들의 합을 계산하는 프로그램을 작성해보자. 내장 함수 sum()은 이용하지 않는다.

myList = [ 11, 22, 23, 99, 81, 93, 35]
sum = 0
for i in myList:
    sum = sum + i
print(f"정수들의 합은 {sum}")