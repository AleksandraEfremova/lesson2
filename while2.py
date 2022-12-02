questions_and_answers = {"Как дела?": "Хорошо!", "Что делаешь?": "Программирую", 'Какой сейчас месяц?': "Декабрь", 'Cколько будет 2+2?': '4'}


def ask_user(user_ask):
    while True:
        user_ask = input('Введите Ваш вопрос: ')
        print(questions_and_answers.get(user_ask))
        

if __name__ == "__main__":
    ask_user(questions_and_answers)



    