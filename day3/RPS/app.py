import random

options = ['가위', '바위', '보']

print('1)가위\n2)바위\n3)보')

human_choice = options[int(input('번호를 선택해주세요')) - 1]
print(f'당신의 선택은 {human_choice}')

computer_choice = random.choice(options)
print(f'컴퓨터의 선택은 {computer_choice}')

if human_choice == '바위':
    if computer_choice == '보':
        print('컴퓨터 승리')
    elif computer_choice == '바위':
        print('비김')
    else:
        print('당신의 승리')

if human_choice == '가위':
    if computer_choice == '바위':
        print('컴퓨터 승리')
    elif computer_choice == '가위':
        print('비김')
    else:
        print('당신의 승리')

if human_choice == '보':
    if computer_choice == '가위':
        print('컴퓨터 승리')
    elif computer_choice == '보':
        print('비김')
    else:
        print('당신의 승리')
