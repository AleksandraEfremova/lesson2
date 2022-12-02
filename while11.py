def hello_user():
    while True:
        ask_user = input('Как дела? ') 
        if ask_user == "Хорошо" :
            break
        else:
            print()
if __name__ == "__main__":
    hello_user()