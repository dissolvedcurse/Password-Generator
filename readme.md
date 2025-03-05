# Генератор случайных паролей

## Описание

Это простая консольная программа на Python, которая генерирует случайные пароли заданной длины и позволяет сохранить их в файл.

## Как использовать

1.  Запустите скрипт `main.py`.
2.  Программа предложит вам ввести длину пароля.
3.  Введите целое число, представляющее желаемую длину пароля (максимум 100).
4.  Программа сгенерирует пароль и предложит сохранить его в файл `passwords.txt`.
5.  Программа предложит вам сгенерировать еще один пароль.

## Зависимости

Для запуска программы требуется установленный интерпретатор Python 3.

## Запуск

1.  Убедитесь, что у вас установлен Python 3.
2.  Сохраните код программы в файл с именем `main.py`.
3.  Откройте терминал или командную строку и перейдите в каталог, где находится файл `main.py`.
4.  Выполните команду `python main.py`.

## Структура проекта

*   `main.py`: Основной файл с кодом программы.
*   `passwords.txt`: Файл, в который сохраняются сгенерированные пароли (создается автоматически).
*   `README.md`: Этот файл с описанием проекта.

## Планируемые улучшения

*   Использовать модуль `secrets` для криптографически стойкой генерации случайных чисел.
*   Добавить возможность выбора набора символов для пароля (буквы, цифры, специальные символы).
*   Реализовать графический интерфейс (GUI) для более удобного использования.
*   Добавить опцию автоматической генерации нескольких паролей.
*   Добавить возможность указания имени файла для сохранения паролей.

## Автор

dissolvedcurse

## Лицензия

MIT License

Copyright (c) 2025 dissolvedcurse

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.