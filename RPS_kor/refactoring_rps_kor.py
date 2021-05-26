from day3.RPS.refactoring_app import start_rps, \
    print_options, print_choice, get_human_choice, get_computer_choice, game_result

OPTIONS = ['가위', '바위', '보']


def choice_turn():
    while True:
        print("턴정하기")
        _winner, _human_choice, _computer_choice = start_rps()
        if not winner == 'draw':
            break
    print(f"{winner}의 턴입니다.")
    return _winner, _human_choice, _computer_choice


def start_game():
    print_options()
    _human_choice = get_human_choice()
    _computer_choice = get_computer_choice()
    print("묵! 찌! 빠!")
    print_choice(human_choice, computer_choice)

    return _human_choice, _computer_choice


if __name__ == "__main__":
    winner, human_choice, computer_choice = choice_turn()

    while True:
        human_choice, computer_choice = start_game()

        if human_choice == computer_choice:
            print(f"{winner}이 승리했습니다.")
            break
        else:
            new_winner = game_result(human_choice, computer_choice)
            if new_winner != winner:
                winner = new_winner
                print(f"턴이 넘어갔습니다. \n{winner}의 턴입니다.")
