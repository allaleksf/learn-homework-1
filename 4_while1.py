"""

Домашнее задание №1

Цикл while: hello_user

* Напишите функцию hello_user(), которая с помощью функции input() спрашивает 
  пользователя “Как дела?”, пока он не ответит “Хорошо”
   
"""


def hello_user():
    """
    Замените pass на ваш код
    """
hello_user()

def hello_user():
    while True:
        pr1 = input("Как дела? ")
        if pr1=="Хорошо":
            print(f"Молодец, раз {pr1}!")
            break

    
if __name__ == "__main__":
    hello_user()
