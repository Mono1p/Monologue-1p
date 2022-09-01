# 사용자가 입력한 정수의 모든 약수를 화면에 출력하는 프로그램을 작성하여 보자.
x = int(input("정수를 입력하시오: "))

for i in range(1, x+1):
    for j in range(1, i+1):
        print(j, end=" ")
    print("")