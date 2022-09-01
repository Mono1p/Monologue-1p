# 문자열이 저장된 리스트를 가정하자. 
# 문자열 중에서 "aba" 처럼 첫 번째 문자와 마지막 문자가 동일한 문자열 수를 계산하는 프로그램을 작성하고 테스트 하라.
x = ['aba', 'xyz', 'abc', '121']
num = 0
for word in x:
    if word[0] == word[-1]:
        num = num+1

print(x)
print("문자열의 개수=", num)