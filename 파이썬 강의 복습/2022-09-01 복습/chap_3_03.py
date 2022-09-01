# 사용자로부터 하나의 문자를 입력받아서 문자가 'R'이나 'r'이면 "Rectangle"이라고 출력한다. 
# 'T'이거나 't'이면 "Triangle", 'C'이거나 'c'이면 "Circle"이라고 출력하는 프로그램을 작성한다. 
# 그 외의 문자가 들어오면 "Unknown"이라고 출력한다.

x = input("문자를 입력하시오: ")
if x == 'R' or x == 'r':
    print("Rectangle")
elif x == 'T' or x == 't':
    print("Triangle")
elif x == 'C' or x == 'c':
    print("Circle")
else:
    print("Unknown")