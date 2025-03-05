import string  # Импортируем модуль string для работы со строками
import random  # Импортируем модуль random для генерации случайных чисел
import os  # Импортируем модуль os для работы с операционной системой
import time  # Импортируем модуль time для добавления задержек

def generate_password(lenght):
    """
    Генерирует случайный пароль заданной длины.

    Args:
        lenght (int): Длина пароля.

    Returns:
        str: Сгенерированный пароль.
    """
    characters = string.ascii_letters + string.digits + string.punctuation  # Определяем набор символов, которые могут быть использованы в пароле (буквы, цифры, знаки препинания)
    password = "" # Инициализируем пустую строку для хранения пароля

    for i in range(lenght):  # Запускаем цикл, который будет выполняться lenght раз
        password += random.choice(characters)  # Добавляем к паролю случайный символ из набора characters
    with open("passwords.txt", "a") as file:  # Открываем файл "passwords.txt" в режиме добавления ("a")
        file.write(f"{password} \n")  # Записываем сгенерированный пароль в файл, добавляя символ новой строки для разделения паролей
    return password  # Возвращаем сгенерированный пароль

def clear_console():
    """
    Очищает консоль.
    """
    time.sleep(2)  # Приостанавливаем выполнение программы на 2 секунды
    os.system("cls" if os.name == "nt" else "clear")  # Выполняем команду очистки консоли, зависящую от операционной системы (cls для Windows, clear для Linux/macOS)

def main():
    """
    Основная функция программы.
    Содержит основной цикл работы программы: запрашивает длину пароля, генерирует его и сохраняет в файл.
    """
    while True:  # Запускаем бесконечный цикл, который будет повторяться до тех пор, пока пользователь не прервет его
        try:
            password_lenght = int(input("Введите длинну пароля: "))  # Запрашиваем у пользователя длину пароля и преобразуем введенное значение в целое число

            if password_lenght < 0:  # Проверяем, является ли введенная длина отрицательной
                print("Ошибка: длинна пароля должна быть положительным числом!")  # Выводим сообщение об ошибке, если длина отрицательная
                clear_console()  # Очищаем консоль
                continue  # Переходим к следующей итерации цикла (начинаем все сначала)
            elif password_lenght > 100:  # Проверяем, не превышает ли введенная длина 100 символов
                print("Ошибка: длинна пароля не должна привышать 100!")  # Выводим сообщение об ошибке, если длина превышает 100
                clear_console()  # Очищаем консоль
                continue  # Переходим к следующей итерации цикла

            generate_password(password_lenght)  # Вызываем функцию для генерации пароля
            print("Пароль успешно сохранён в passwords.txt!")  # Выводим сообщение об успешном сохранении пароля
            clear_console()  # Очищаем консоль
        except ValueError:  # Обрабатываем исключение ValueError, которое может возникнуть, если пользователь введет не число
            print("Ошибка: разрешено вводить только целые числа!")  # Выводим сообщение об ошибке
            clear_console()  # Очищаем консоль

if __name__ == "__main__":
    main()  # Запускаем основную функцию, если скрипт запущен напрямую (не импортирован как модуль)