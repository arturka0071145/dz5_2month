from game_logic import generate_winning_slot,check_win
from main import initial_capital

def play_game():
    available_money = initial_capital  #начальный капитал
    while True:
        if available_money == 0:
            break
        print(f"Ваш доступный капитал: { available_money}$")
        while True:
            try:
                selected_number = int(input(f'введите число 1-30:'))
                if selected_number > 30 or selected_number < 1:
                    print(f' Пожалуйста, введите правильный номер слота')
                else:
                    break

            except:
                  ValueError
                  print(f'неверный номер слота!! пожалуйста, введите номер слота')


        your_rate = int(input("введите свою ставку:"))
        winning_number = generate_winning_slot()
        if check_win(selected_number,winning_number):
            available_money += your_rate * 2
            print(f" Вы выйграли!{winning_number} Выйгрышний слот")
        else:
            available_money -= your_rate
            print(f" Вы проиграли! {winning_number} Выйгрышний слот")

        new_game = input("Хотите продолжить? (y or n): ")
        if  new_game.lower() != 'y':
            break
    print(f"Конец игры. Ваш счет: { available_money}$")

play_game()