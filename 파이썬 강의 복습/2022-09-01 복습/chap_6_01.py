# 사용자가 입력하는 정수값을 리스트에 저장하고 이 값들의 합계를 계산하는 프로그램을 작성해보자.

num = []
x = int(input("입력할 값의 개수: "))
for i in range(1,x+1):
    num.append(int(input("")))

print("값의 합계=", sum(num[:]))