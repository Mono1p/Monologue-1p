# 컴퓨터와 가위, 바위, 보 게임을 하는 프로그램을 작성하라. 
# 컴퓨터는 사용자에게 알리지 않고 가위, 바위, 보 중에서 임의로 하나를 선택한다. 
# 사용자는 프로그램의 입력 안내 메시지에 따라서, 3개 중에 하나를 선택하게 된다. 
# 사용자의 선택이 끝나면 컴퓨터는 누가 무엇을 선택하였고 누가 이겼는지, 비겼는지를 알려준다.

import random

user_choice = int(input("선택하시오(1: 가위 2:바위 3:보 ) "))
comp_choice = random.randint(1,3)

print(f"컴퓨터의 선택(1: 가위 2:바위 3:보 ) {comp_choice}")
if (user_choice == 1 and comp_choice == 3) or (user_choice == 2 and comp_choice == 1) or (user_choice == 3 and comp_choice == 2):
    print("유저가 이겼음.")
elif (user_choice == 1 and comp_choice == 2) or (user_choice == 2 and comp_choice == 3) or (user_choice == 3 and comp_choice == 1):
    print("컴퓨터가 이겼음.")
elif user_choice == comp_choice:
    print("비겼음.")
else:
    print("잘못된 값입니다.")