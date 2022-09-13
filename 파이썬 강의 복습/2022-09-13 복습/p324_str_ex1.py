#사용자로부터 2개의 문자열을 받아서 두 문자열의 공통 문자를 출력하는 프로그램

s1 = input("첫 번째 문자열 : ")
s2 = input("두 번째 문자열 : ")

x = list((set(s1) & set(s2)))
print("\n공통적인 글자 : ",end=" ")
for i in x:
    print(i, end=" ")