# 원의 넓이를 계산하느 프로그램에서 사용자가 입력한 원의 반지름을 검증해보자.
# 사용자가 입력한 값이 음수이면 "잘못된 값입니다"를 출력하도록 프로그램을 작성해보자.

r = int(input("원의 반지름: "))
if r >= 0:
    print(r*r*3.14)
else:
    print("잘못된 값입니다.")