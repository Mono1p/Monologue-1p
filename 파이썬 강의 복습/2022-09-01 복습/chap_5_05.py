# 패스워드를 검증하는 함수 checkPass(p)를 작성하고 테스트 하라.
# 패스워드에는 적어도 8글자 이상이어야 한다.
# 또 적어도 1글자의 대문자와 소문자가 들어가야 한다. 또 적어도 1개의 숫자가 들어가야 한다.

import re

def checkPass(p):
    if len(p) < 8 or not re.findall('[0-9]+', p) or not re.findall('[a-z]', p) or not re.findall('[A-Z]', p):
        print("사용할 수 없습니다. 다시 입력하세요!")
        return False
    else:
        print("사용할 수 있습니다.")
        return True


x = input("패스워드를 입력하시오: ")
checkPass(x)