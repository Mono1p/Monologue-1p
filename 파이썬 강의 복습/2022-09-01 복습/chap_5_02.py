# 덧셈, 뺄셈, 곱셈, 나눗셈을 수행하는 함수를 각각 작성하고 테스트하라.

from ast import Add
from operator import add

def add(a,b):
    return a + b

def sub(a,b):
    return a - b

def mul(a,b):
    return a * b

def div(a, b):
    return a / b

x = int(input("첫 번째 정수를 입력하시오: "))
y = int(input("두 번째 정수를 입력하시오: "))

print(add(x,y))
print(sub(x,y))
print(mul(x,y))
print(div(x,y))