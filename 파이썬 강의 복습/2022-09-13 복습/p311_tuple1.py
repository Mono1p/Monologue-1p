#튜플 : 리스트와 유사하나 변경이 불가능 함.
fruits = ()                             #공백 튜플을 생성한다.
fruits = ("apple", "banana", "grape")   #초기값을 가진 튜플을 생성한다.

result = fruits[1]                      #인덱스를 사용하여 요소에 접근한다.


single_tuple = ("apple",)       #요소가 하나 뿐인 튜플을 만들 때에서는 요소 끝에 반드시 쉼표(,)를 추가하여야 한다.
no_tuple = ("apple")            #쉼표가 없으면 튜플이 아니라 수식이 된다.


myList = [1,2,3,4]
myTuple = tuple(myList)         #tuple() : 튜플을 생성하는 함수
print(myTuple)

myTuple = (1,2,3,4)
myList = list(myTuple)          #lsit() : 리스트를 생성하는 함수
print(myList)