import random, time

def player_rolls():
    while True:
        x  = input("Окей, кидай кубик ('кинуть'): ").lower()
        match x:
            case 'кинуть':
                player_result = random.randint(1,6)
                print(f'У тебя {player_result}, теперь кидаю я')
                time.sleep(1)
                computer_result = random.randint(1,6)
                if player_result > computer_result:
                    print(f"У меня {computer_result}. \nПоздравляю! Ты победил")
                elif player_result == computer_result:
                    print(f"Ничья, у обоих по {computer_result}")
                else:
                    print(f"У меня {computer_result}, я победил :>")
                break
            case other:
                continue

def computer_rolls():
    while True:
        print('Хорошо! Я хожу первым')
        time.sleep(1)
        computer_result = random.randint(1,6)
        z = input(f'У меня {computer_result}, теперь кидай ты (\'кинуть\'): ').lower()
        time.sleep(1)
        match z:
            case 'кинуть':
                player_result = random.randint(1,6)
                if player_result > computer_result:
                    print(f'У тебя {player_result}, поздравляю, ты победил!')
                elif player_result == computer_result:
                    print(f'У нас обоих по {player_result}, ничья')
                else:
                    print(f'У тебя {player_result}, ты проиграл(')
                break
            case other:
                continue

while True:
    greet = input("Выбирай кто ходит первым, ты или я: ").lower()
    match greet:
        case 'я':
            player_rolls()
            break
        case 'ты':
            computer_rolls()
            break
        case other:
            continue