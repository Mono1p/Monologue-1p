# 본문에서 덧셈 퀴즈를 자동으로 생성해보았다. 
# 이번에는 덧셈, 뺄셈, 곱셈, 나눗셈 중에서 하나를 랜덤하게 선택하고 
# 피연산자도 난수로 생성하여 사용자에게 제시하고 사용자의 답을 자동으로 채점하는 프로그램을 작성해보자.

import random

while True:
    x = random.randint(1,10)
    y = random.randint(1,10)
    a = random.randint(1,4)
    
    if a == 1: #덧셈
        user = int(input(f"{x} + {y}의 값은? "))
        if user == x + y:
            print("맞았습니다.")
        else:
            print("틀렸습니다.")
            break

    elif a == 2: #뺄셈
        user = int(input(f"{x} - {y}의 값은? "))
        if user == x - y:
             print("맞았습니다.")
        else:
            print("틀렸습니다.")
            break

    elif a == 3: #곱셈
        user = int(input(f"{x} * {y}의 값은? "))
        if user == x * y:
            print("맞았습니다.")
        else:
            print("틀렸습니다.")
            break

    else:
        user = int(input(f"{x} / {y}의 값은? "))
        if user == x / y:
            print("맞았습니다.")
        else:
            print("틀렸습니다.")
            break
