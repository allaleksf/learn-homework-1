#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""

Домашнее задание №1

Исключения: KeyboardInterrupt

* Перепишите функцию hello_user() из задания while1, чтобы она 
  перехватывала KeyboardInterrupt, писала пользователю "Пока!" 
  и завершала работу при помощи оператора break
    
"""

def hello_user():
    """
    Замените pass на ваш код
    """
    while True:
        try:
            pr1 = input("Как дела? ")
            if pr1 == "Хорошо":
                print("Молодец, раз так!")
                break
        except KeyboardInterrupt:
            print("что так?")
    
if __name__ == "__main__":
    hello_user()
