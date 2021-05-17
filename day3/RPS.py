import random

ATTACK = 0
OPTIONS = {'가위': {'win': '보', 'lose': '바위'},
           '바위': {'win': '가위', 'lose': '보'},
           '보': {'win': '바위', 'lose': '가위'}}
GAME_LAST = 0

def print_options():
    print('\n'.join(f'({i}) {option.title()}' for i, option in enumerate(list(OPTIONS.keys()), 1)))


def get_computer_choice():
    return random.choice(list(OPTIONS.keys()))


def get_human_choice():
    choice_number = int(input('번호 를 선택해 주세요'))
    return list(OPTIONS.keys())[choice_number - 1]


def print_choice(human_choice, computer_choice):
    print('당신의 선택은 {}'.format(human_choice))
    print('컴퓨터 선택은 {}'.format(computer_choice))


def print_who_attack(human_choice, computer_choice):
    global ATTACK
    human_beats = OPTIONS[human_choice]['win']
    human_loses_to = OPTIONS[human_choice]['lose']

    if computer_choice == human_loses_to:
        print('컴퓨터 공격')
        ATTACK = -1
    elif computer_choice == human_beats:
        print('당신의 공격')
        ATTACK = 1
    else:
        print('다시')
        ATTACK = 0


def print_result(human_choice, computer_choice):
    global GAME_LAST
    human_beats = OPTIONS[human_choice]['win']
    human_loses_to = OPTIONS[human_choice]['lose']

    if computer_choice == human_loses_to:
        print('컴퓨터 공격')
        ATTACK = -1

    elif computer_choice == human_beats:
        print('당신의 공격')
        ATTACK = 1

    elif human_choice == computer_choice:
        print('게임종료')
        GAME_LAST = 1


def attacker_choice():
    human_choice = get_human_choice()
    computer_choice = get_computer_choice()
    print_choice(human_choice, computer_choice)
    print_who_attack(human_choice, computer_choice)


def start_game():
    human_choice = get_human_choice()
    computer_choice = get_computer_choice()
    print_choice(human_choice, computer_choice)
    print_result(human_choice, computer_choice)


print_options()
while ATTACK == 0:
    attacker_choice()

while ATTACK != 0:
    start_game()
    if GAME_LAST == 1:
        break

if ATTACK == -1:
    print('컴퓨터 승리')
elif ATTACK == 1:
    print('당신의 승리')