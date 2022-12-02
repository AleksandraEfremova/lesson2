def main(a,b):
    if  a != str(a) and b != str(a):
        return 0
    elif str(a) == str(b):
        return 1
    elif a != b and len(a)>len(b):
        return 2
    elif a != b and b == "learn":
        return 3
if __name__ == "__main__":
        print(main(3,'pyhton'))
        print(main("learn",'learn'))
        print(main('pyhtonn','pyhton'))
        print(main('py','learn'))