fruits = {"apple", "banana", "grape"}

fruits.add("kiwi")          #add() 메소드를 이용하여 요소를 추가한다.
print(fruits)

fruits.remove("kiwi")       #remove() 메소드로 요소를 삭제한다.
print(fruits)

#fruits.remove("mango")     #remove() 메소드는 삭제하고자 하는 요소가 없으면 오류를 생성한다.
fruits.discard("mango")     #discard() 메소드는 삭제하고자 하는 요소가 없으면 그냥 넘어간다.

fruits.clear()              #리스트를 초기화 시킨다. (세트의 모든 요소 삭제)
print(fruits)