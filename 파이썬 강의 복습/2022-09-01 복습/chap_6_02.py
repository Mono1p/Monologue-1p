# 1부터 100 사이의 난수 10개를 생성하여 리스트 values를 채우는 반복 루프를 작성하라.
import random
values = [random.randint(1,100) for i in range(10)]

print(values)