# 사용자로부터 3개의 정수를 읽어 들인 후에 if~else 문을 사용하여 가장 작은 값을 결정하는 프로그램을 작성하라.

x, y, z =input("3개의 정수를 입력하시오: ").split(", ")

if x > y:
    min = y
else:
    min = x

if min > z:
    min = z

print(f"제일 작은 정수는 {min}입니다.")