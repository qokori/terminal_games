from subprocess import call
import time

while True:
    greet = input("""
Привет! Выбери один из пунктов для продолжения
1 - 'Sosal' test
2 - RNG dice
3 - Выйти

""");
    match greet:
        case '1':
            print("Запускаем.. \n")
            time.sleep(1)
            call(["python", "sosal-test.py"]) #type: ignore
            break
        case '2':
            print("Запускаем.. \n")
            time.sleep(1)
            call(["python", "rng.py"])
            break
        case '3':
            exit()
        case other:
            continue