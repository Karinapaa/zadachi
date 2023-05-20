do = input("Выберите операцию: +, -, /, *, возведение в степень, модуль, рандомное число, факториал и арккосинус: ")
while do != "stop":
    if do == "+":
        number1 = float(input("1 значение: "))
        number2 = float(input("2 значение: "))
        print(number1 + number2)
    elif do == "-":
        number1 = float(input("1 значение: "))
        number2 = float(input("2 значение: "))
        print(number1 - number2)
    elif do == "/":
        number1 = float(input("1 значение: "))
        number2 = float(input("2 значение: "))
        if number2 != 0:
            print(number1 / number2)
        else:
            print("на 0 делить нельзя")
    elif do == "*":
        number1 = float(input("1 значение: "))
        number2 = float(input("2 значение: "))
        print(number1 * number2)
    elif do == "pow": #возведение в степень
        number1 = float(input("1 значение: "))
        number2 = float(input("2 значение: "))
        print(pow(number1, number2))
    elif do == "module": #модуль
        number1 = float(input("значение: "))
        print(abs(number1))
    elif do == "0": #рандомное число
        print(random.randint(0, 1000))
    elif do == "f": #факториал
        number1 = int(input("значение: "))
        print(math.factorial(number1))
    elif do == "arccos": #арккосинус
        number1 = float(input("значение: "))
        number11 = number1*math.pi/180
        print(math.acos(number11))
    do = input("Для продолжения введите следующую операцию или напишите stop, чтобы завершить работу калькулятора: ")