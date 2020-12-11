#!/usr/bin/env python3
# Игра "Русская рулетка"
# Версия 1.0

#Импортируем модуль рандома
import random

# Заголовок
print("Добро пожаловать в игру \"Русская рулетка\"")
print("Версия: 1.0")

# Узнаем имя игрока и приветствуем его
name=input("\nВведите ваше имя: ")
print("\nОтлично, " + name + ", начинаем игру...")

# Узнаем желает ли игрок переиграть или выйти из игры
def exit_code():    
    answer=input("\nЧтобы переиграть, введите R. Для выхода из игры нажмите Enter: ")
    if answer.upper() == "R": 
        print("\nОтлично, " + name + ", начинаем игру...")
        coin_game()
    else:
        exit()

# Создаем основную функцию игры в случае угадывания игроком монетки 
def main():
    # Первый раунд
    print("\n===ПЕРВЫЙ РАУНД===")
    print("\nВставляем в револьвер одну пулю. Раскручиваем барабан...")
    print("\nВнимание! Ваш ход...")
    input("\nНажмите Enter чтобы спустить курок...")
    raund1_player=random.randint(1,6)
    if raund1_player == 6:
        print("\nВы вышибли себе мозги! :(")
        exit_code()
    else:
        print("\nВы спустили курок, но ничего не произошло. Ура!!!")
        print("\nТеперь ход вашего противника.")
    input("\nНажмите Enter для передачи хода противнику...")
    raund1_comp=random.randint(1,5)
    if raund1_comp == 5:
        print("\nВаш противник вышиб себе мозги!!! Вы победили!!! Наши поздравления!!!")
        exit_code()
    else:
          print("\nВаш противник спустил курок, но ничего не произошло.")
          print("\nПришло время для второго раунда.")
    input("\nНажмите Enter для начала второго раунда...")

    # Второй раунд
    print("\n===ВТОРОЙ РАУНД===")
    print("\nВнимание! Ваш ход...")
    input("\nНажмите Enter чтобы спустить курок...")
    raund2_player=random.randint(1,4)
    if raund2_player == 4:
        print("\nВы вышибли себе мозги! :(")
        exit_code()
    else:
        print("\nВы спустили курок, но ничего не произошло. Ура!!!")
        print("\nТеперь ход вашего противника.") 
    input("\nНажмите Enter для передачи хода противнику...")
    raund2_comp=random.randint(1,3)
    if raund2_comp == 3:
        print("\nВаш противник вышиб себе мозги!!! Вы победили!!! Наши поздравления!!!")
        exit_code()
    else:
        print("\nВаш противник спустил курок, но ничего не произошло.")
        print("\nПришло время для решающего раунда.")
    input("\nНажмите Enter для начала решающего раунда...")  

    # Третий раунд
    print("\n===РЕШАЮЩИЙ РАУНД===")
    print("\nВнимание! Ваш ход...")
    input("\nНажмите Enter чтобы спустить курок...")
    raund3_player=random.randint(1,2)
    if raund3_player == 2:
        print("\nВы вышибли себе мозги! :(")
        exit_code()
    else:
        print("\nВы спустили курок, но ничего не произошло. Ура!!!")
        print("\nТеперь ход вашего противника.")
    input("\nНажмите Enter для передачи хода противнику...")
    print("\nВаш противник берет револьвер, смотрит на него обреченно, прикладывает к виску и спускает курок! Его мозги разлетаются по всей комнате!")     
    print("\nВы победили!!! Наши поздравления!!!")
    exit_code() 

# Создаем альтернативную функцию игры в случае проигрыша игрока в угадывании монетки
def main_alt():
    # Первый раунд
    print("\n===ПЕРВЫЙ РАУНД===")
    print("\nВставляем в револьвер одну пулю. Раскручиваем барабан...")
    alt_raund1_comp=random.randint(1,6)
    if alt_raund1_comp == 6:
        print("\nВаш противник вышиб себе мозги!!! Вы победили!!! Наши поздравления!!!")
        exit_code()
    else:
        print("\nВаш противник спустил курок, но ничего не произошло.")
        print("\nТеперь ваш ход. Вы берете револьвер...")
    input("\nНажмите Enter чтобы спустить курок...")
    alt_raund1_player=random.randint(1,5)
    if alt_raund1_player == 5:
        print("\nВы вышибли себе мозги! :(")
        exit_code()
    else:
          print("\nВы спустили курок, но ничего не произошло. Ура!!!")
          print("\nПришло время для второго раунда.")
    input("\nНажмите Enter для начала второго раунда...")

    # Второй раунд
    print("\n===ВТОРОЙ РАУНД===")
    alt_raund2_comp=random.randint(1,4)
    if alt_raund2_comp == 4:
        print("\nВаш противник вышиб себе мозги!!! Вы победили!!! Наши поздравления!!!")
        exit_code()
    else:
        print("\nВаш противник спустил курок, но ничего не произошло.")
        print("\nТеперь ваш ход. Вы берете револьвер...")
    input("\nНажмите Enter чтобы cпустить курок...")
    alt_raund2_player=random.randint(1,3)
    if alt_raund2_player == 3:
        print("\nВы вышибли себе мозги! :(")
        exit_code()
    else:
        print("\nВы спустили курок, но ничего не произошло. Ура!!!")
        print("\nПришло время для решающего раунда.")
    input("\nНажмите Enter для начала решающего раунда...")  

    # Третий раунд
    print("\n===РЕШАЮЩИЙ РАУНД===")
    alt_raund3_comp=random.randint(1,2)
    if alt_raund3_comp == 2:
        print("\nВаш противник вышиб себе мозги!!! Вы победили!!! Наши поздравления!!!")
        exit_code()
    else:
        print("\nВаш противник спустил курок, но ничего не произошло.")
        print("\nТеперь ваш ход.")
    input("\nНажмите Enter чтобы взять револьвер...")
    print("\nВы берете револьвер, смотрите на него обреченно, прикладываете к виску и спускаете курок! Ваши мозги разлетаются по всей комнате!")     
    print("\nВы проиграли. Такое случается...")
    exit_code() 


# Мини-игра с монеткой для определения того кто начнет играть первым
def coin_game():
    print("\nИтак, определим кто начнет первым...")
    print("\nПодкидываем монетку...")
    coin=random.randint(1,2)
    print("\n===ВАРИАНТЫ===")
    print("\nЕсли считаете что выпал орел введите: 1")
    print("\nЕсли считаете что выпала решка введите: 2")
    while True:
        try:
            choice=int(input("\nВведите свой выбор: "))
            if choice == 1:
                break
            elif choice == 2:
                break
            else:
                print("\nВы должны ввести либо 1(орел) либо 2(решка)")
        except ValueError:
            print("\nВы должны ввести либо 1(орел) либо 2(решка)")    
    if choice == coin:
        print("\nВы угадали! Значит начинаете первым...")
        main()
    else:
        print("\nВы ошиблись! Придется вам начинать вторым...")
        main_alt()

# Старт игры
coin_game()
