# while 루프를 이용하여서 (n**2 > 500)인 n 중에서 가장 작은 n을 찾는 프로그램을 작성하시오.

n = 1
while n**2 < 500:
    n = n + 1
else:
    print(n, n**2)