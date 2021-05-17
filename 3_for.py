"""

Домашнее задание №1

Цикл for: Оценки

* Создать список из словарей с оценками учеников разных классов 
  школы вида [{'school_class': '4a', 'scores': [3,4,4,5,2]}, ...]
* Посчитать и вывести средний балл по всей школе.
* Посчитать и вывести средний балл по каждому классу.
"""
import statistics

def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    sh_list=[
    {'school_class': '4a', 'scores': [3,4,4,5,2]},
    {'school_class': '4b', 'scores': [4,5,5,5,2]},
    {'school_class': '4с', 'scores': [2,3,4,5,5]}
    ]

    avr1=[]

    for i in range(len(sh_list)):
        cl1=(sh_list[i])
        print("у класса",cl1['school_class'])
        print("средняя оценка",statistics.mean(cl1['scores']))
        i=i+1
        avr1.extend(cl1['scores'])

    print("средний балл по всей школе",statistics.mean(avr1))


if __name__ == "__main__":
    main()
