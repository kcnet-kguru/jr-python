import random

OPTIONS = ['가위', '바위', '보']


def print_options():
    print('\n'.join([f"{i+1}) {option}" for i, option in enumerate(OPTIONS)]))


def get_computer_choice():
    return random.choice(OPTIONS)


def get_human_choice():
    choice_number = int(input('번호를 선택해 주세요: '))
    return OPTIONS[choice_number - 1]


def print_choice(human_choice, computer_choice):
    print(f"당신의 선택은 {human_choice}")
    print(f"컴퓨터의 선택은 {computer_choice}")


def who_is_winner(computer_choice, human_beats, human_lose_to):
    if computer_choice == human_lose_to:
        # print(f'컴퓨터 승리!!!')
        return "com"
    elif computer_choice == human_beats:
        # print(f'당신이 이겼습니다.')
        return "human"


def game_result(human_choice, computer_choice):
    if human_choice == computer_choice:
        # print('비겼습니다.')
        return "draw"

    if human_choice == '바위':
        return who_is_winner(computer_choice, '가위', '보')
    elif human_choice == '보':
        return who_is_winner(computer_choice, '바위', '가위')
    elif human_choice == '가위':
        return who_is_winner(computer_choice, '보', '바위')


def start_rps():
    print_options()
    _human_choice = get_human_choice()
    _computer_choice = get_computer_choice()
    print_choice(_human_choice, _computer_choice)
    return game_result(_human_choice, _computer_choice), _human_choice, _computer_choice
