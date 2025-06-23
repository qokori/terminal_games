import random, time

answer = ""
second_answer = ""

while True:
    answer = input("сосал? Только честно \n").lower()
    match answer:
        case "да":
            print("еб..ть💀")
            exit()
        case "нет":
            break
        case other:
            continue

def test_if_pizdabol():
    roll = random.randint(1,100)
    if roll >= 70:
        print(f"ладно, верю ({roll}/100)")
    else:
        print(f"депортировать ({roll}/100)")

while True:
    second_answer = input("сука пиздишь же \n").lower()
    match second_answer:
        case "да":
            print("пизда")
            break
        case "нет":
            print("сейчас и узнаем нахуй")
            time.sleep(1)
            print("роллим...")
            time.sleep(1)
            test_if_pizdabol()
            break
        case other:
            continue

