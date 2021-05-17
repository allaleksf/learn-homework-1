"""

Домашнее задание №1

Цикл while: ask_user со словарём

* Создайте словарь типа "вопрос": "ответ", например:
  {"Как дела": "Хорошо!", "Что делаешь?": "Программирую"} и так далее
* Напишите функцию ask_user() которая с помощью функции input()
  просит пользователя ввести вопрос, а затем, если вопрос есть
  в словаре, программа давала ему соотвествующий ответ. Например:

    Пользователь: Что делаешь?
    Программа: Программирую
    
"""

questions_and_answers = {
    "как дела": "Хорошо!",
    "что делаешь": "Программирую",
    "получается": "не очень",
    "что так":"норм",
}


def ask_user(answers_dict):
    """
    Замените pass на ваш код
    que1 = input("Спроси меня: ")
    for key in questions_and_answers:
        if key == que1:
            print("ответ:", questions_and_answers[key])
    else:
        print("ответ: не знаю")
"""

    while True:
        que1 = input("Спроси меня: ")
        if que1 in questions_and_answers:
            print(questions_and_answers[que1])

        if que1 not in questions_and_answers:
            exit("ответ: не знаю")

if __name__ == "__main__":
    ask_user(questions_and_answers)
