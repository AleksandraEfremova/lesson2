def hello_user():
    try:
        while True: 
            ask_user = input('Как дела? ')
            if ask_user == "Хорошо" :
                break
            else:
                print()
    except KeyboardInterrupt:
        print('Пока')
        

if __name__ == "__main__":
    hello_user()

