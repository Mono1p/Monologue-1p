fruits = {"apple", "banana", "grape"}
size = len(fruits)          #size = 3


if "apple" in fruits:                       #어떤 항목이 세트 안에 있는지를 검사하여면 in 연산자 사용
    print("집합 안에 apple이 있습니다.") 



for x in fruits:            #for 반복문을 이용하여 각 항목에 접근할 수 있다. 순서없이 출력
    print(x, end=" ")


for x in sorted(fruits):        #정렬을 한 후 출력한다.
    print(x, end=" ")