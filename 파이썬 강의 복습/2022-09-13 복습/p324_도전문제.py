#2개의 문자열을 비교했을 때, 공통적인 글자가 많으면 표절이라고 의심할 수도 있다. 공통적인 문자의 비율이 전체 문자의 70% 이상이 되면 "표절 의심"이라고 출력해보자.

s1 = input("첫 번째 문자열 : ")
s2 = input("두 번째 문자열 : ")

x = list(set(s1) & set(s2))

if len(x) >= len(set(s1) | set(s1)) * 0.7 :
    print("표절 의심") 