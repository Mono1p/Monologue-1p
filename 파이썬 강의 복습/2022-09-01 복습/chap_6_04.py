# 리스트 함축을 이용하여 다음과 같은 실행 결과가 나오도록 프로그램을 작성하라.

x = [i for i in range(1,11)]
x1 = [(-1)*i if 3 <= i <= 8 else i for i in range(1,11)]

print("실행전", x)
print("실행후", x1)