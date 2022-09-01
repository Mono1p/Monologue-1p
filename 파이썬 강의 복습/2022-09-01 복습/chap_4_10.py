# 1**2+2**2+3**2*...n**2의 값을 계산하여 출력하여 보자.

n = int(input("n의 값을 입력하시오: "))

sum = 0
for i in range(1,n+1):
    sum = sum + i**2

print(f"계산값은 {sum}입니다.")
