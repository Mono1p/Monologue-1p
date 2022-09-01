# 2와 20 사이에 있는 모든 소수를 찾는 프로그램을 작성하라. 
# 정수가 소수가 되려면 1과 자기 자신만을 약수로 가져야 한다.

for i in range(2, 21):
    x = True
    for j in range(2, i):
        if i % j == 0:
            x = False
            break
    if x:
        print(i, end=" ")
