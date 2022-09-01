# 하나의 함수 calc() 안에서 덧셈, 뺄셈, 곱셈, 나눗셈을 모두 수행하고 4개의 계산값을 동시에 반환하도록 수정해보자.

def calc(a, b):
    return a+b, a-b, a*b, a/b

x = int(input("첫 번째 정수를 입력하시오: "))
y = int(input("두 번째 정수를 입력하시오: "))

print(calc(x,y),"이 반환되었습니다.")