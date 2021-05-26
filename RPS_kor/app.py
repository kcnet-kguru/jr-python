import random
from day3.RPS.refactoring_app import start_rps, \
    print_options, print_choice, get_human_choice, get_computer_choice, game_result

OPTIONS = ['가위', '바위', '보']

if __name__ == "__main__":
    while True:
        print("턴정하기")
        winner, human_choice, computer_choice = start_rps()
        if not winner == 'draw':
            break
    print(f"{winner}의 턴입니다.")

    while True:
        print_options()
        human_choice = get_human_choice()
        computer_choice = get_computer_choice()
        print("묵! 찌! 빠!")
        print_choice(human_choice, computer_choice)

        if human_choice == computer_choice:
            print(f"{winner}이 승리했습니다.")
            break
        else:
            new_winner = game_result(human_choice, computer_choice)
            if new_winner != winner:
                winner = new_winner
                print(f"턴이 넘어갔습니다. \n {winner}의 턴입니다.")
