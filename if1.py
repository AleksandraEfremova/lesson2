userage=input('Введите Ваш возраст  ')

def main(userage):
    userage=int(userage)
    if 3 <= userage < 7:
        return 'Вы должны учиться в детском саду'
    if 7 <= userage <= 17:
        return 'Вы должны учиться в школе'
    if 17 <= userage <= 22:
        return 'Вы должны учиться в ВУЗе'
    if 22 <= userage < 65: 
        return 'Вы должны работать'  
    else:
        return "Вы никому ничего не должны"
if __name__ == "__main__":
    print (main(userage))