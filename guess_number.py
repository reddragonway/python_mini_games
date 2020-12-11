#!/usr/bin/env python3
# Игра "Отгадай число"
# Версия 1.0

# Импортируем модуль рандома
import random

# Заголовок
print("Добро пожаловать в игру \"ОТГАДАЙ ЧИСЛО\"")
print("Версия: 1.0")

# Узнаем имя игрока
name=input("\nВведите ваше имя: ")

# Создаем основную функцию игры
def main():
    
    # Информируем о начале игры  
    print("\nОтлично, " + name + ", начинаем игру...")
    print("\nЯ загадал число от 1 до 100. Постарайтесь отгадать его за минимальное число попыток.")

    # Начальные значение
    number=random.randint(1,100) # выбираем случайное число от 1 до 100
    while True:  # обрабатываем исключение ValueError (если игрок ввел буквы, а не цифры)
            try:
                guess=int(input("\nВаше предположение: "))
                if (guess > 0 and guess <= 100):
                    break
                else:
                    print("\nВведите число от 1 до 100!")
            except ValueError:
                print("\nВведите число от 1 до 100!")
    tries=1   # устанавливаем число попыток на 1

    # Цикл отгадывания
    while guess != number:
        if guess > number:
            print("\nМеньше...")
        else:
            print("\nБольше...")
        while True:  # обрабатываем исключение ValueError (если игрок ввел буквы, а не цифры)
            try:
                guess=int(input("\nВаше предположение: "))
                if (guess > 0 and guess <= 100):
                    break
                else:
                    print("\nВведите число от 1 до 100!")
            except ValueError:
                print("\nВведите число от 1 до 100!")
        tries+=1  # увеличиваем число попыток на 1
    print("\nПоздравляем, " + name+ "! Вам удалось отгадать число! Это действительно",number,":)")
    print("\nВы смогли угадать загаданное число с", tries, "попыток.")

    # Узнаем желает ли игрок переиграть или выйти из игры
    answer=input("\nЧтобы переиграть, введите R. Для выхода из игры нажмите Enter: ")  
    if answer.upper() == "R": 
        main()                
    else:                       
        exit()                 

# запуск игры
main()                        # запускаем основную функцию игры   

