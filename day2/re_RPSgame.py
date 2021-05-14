import random

OPTIONS = {'가위':['보', '바위'], '바위':['가위', '보'], '보':['바위', '가위']}


def print_options():
    print('\n'.join(f'({i}) {option.title()}' for i, option in enumerate(list(OPTIONS.keys()), 1)))

def get_computer_choice():
    return random.choice(OPTIONS)

def get_human_choice():
    choice_number = int(input('번호를 선택해 주세요'))
    return OPTIONS[choice_number - 1]

def print_choice(human_choice, computer_choice):
    print('당신의 선택은 {}'.format(human_choice))
    print('컴퓨터 선택은 {}'.format(computer_choice))

def print_win_lose(human_choice, computer_choice):
    human_beats = OPTIONS[human_choice][0]
    human_loses_to = OPTIONS[human_choice][1]

    if computer_choice == human_loses_to:
        print('컴퓨터 승리')
    elif computer_choice == human_beats:
        print('당신의 승리')
    else:
        print('비김')

print_options()
human_choice = get_human_choice()
computer_choice = get_computer_choice()
print_choice(human_choice, computer_choice)
print_win_lose(human_choice, computer_choice)



