import random

options = ('가위', '바위', '보')

print('(1) 가위\n (2) 바위\n (3) 보')

human_choice = options[int(input('번호를 선택해 주세요')) - 1]
print('당신의 선택은 {}'.format(human_choice))

computer_choice = random.choice(options)
print('컴퓨터의 선택은 {}'.format(computer_choice))

if human_choice == '바위':
    if computer_choice == '보':
        print('컴퓨터 승리')
    elif computer_choice == '가위':
        print('당신의 승리')
    elif computer_choice == '바위':
        print('둘이 비겼음')

elif human_choice == '가위':
    if computer_choice == '보':
        print('당신의 승리')
    elif computer_choice == '가위':
        print('둘이 비겼음')
    elif computer_choice == '바위':
        print('컴퓨터 승리')

elif human_choice == '보':
    if computer_choice == '보':
        print('둘이 비겼음')
    elif computer_choice == '가위':
        print('컴퓨터 승리')
    elif computer_choice == '바위':
        print('당신의 승리')