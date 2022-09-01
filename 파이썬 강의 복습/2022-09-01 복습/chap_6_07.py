# 다음과 같은 리스트를 생성하고 리스트에서 무작위로 항목을 선택하는 프로그램을 작성해보자.
import random
list1 = ['a0', 'a1', 'a2', 'a3', 'a4', 'a5', 'a6', 'a7', 'a8', 'a9']
print(list1[random.randint(0, 8)])