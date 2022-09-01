# 사용자로부터 2개의 정수를 받아서 수학 문제를 만들어서 화면에 출력하는 함수를 작성하고 테스트하시오.

import random

def my_math(a, b):
    t = True
    op = random.randint(1,4)
    if op == 1:
        answer = int(input(f"정수 {a} + {b}의 합은? "))
        if answer != x + y:
            t = False
    elif op == 2:
        answer = int(input(f"정수 {a} - {b}의 차은? "))
        if answer != x - y:
            t = False
    elif op == 3:
        answer = int(input(f"정수 {a} x {b}의 곱은? "))
        if answer != x * y:
            t = False
    else:
        answer = float(input(f"정수 {a} / {b}의 나누기는? "))
        if answer != x / y:
            t = False
    
    if t == True:
        print("맞췄습니다.")
    else:
        print("틀렸습니다.")


x = int(input("첫 번째 정수를 입력하시오: "))
y = int(input("두 번째 정수를 입력하시오: "))

my_math(x,y)
