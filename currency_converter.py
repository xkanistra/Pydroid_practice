# Конвертер валют из Рос.руб в Доллар/Евро

DOLLAR = 90.5
EURO = 98.2

def main():
    print('-' * 5, "Конвертер валют", '-' * 5)
    money = get_money()
    value = get_value()
    result = convert(money, value)
    print_result(result, value)

# Функция получает сумму денег для перевода 
def get_money():
    result = float(input("Введите сумму денег для перевода: "))
    while True:
        if result < 0:
            print('ОШИБКА! Неверное значение')
            result = float(input('Введите верное значение:  '))
        else:
            break
    return result

# Функция выбора валюты в которую будет происходить перевод
def get_value():
    print("1 - USD, 2 - EUR")
    result = int(input("Выберите валюту для перевода: "))
    while True:
        if result < 1 or result > 2:
            print('ОШИБКА! Неверное значение')
            result = int(input('Введите верное значение (1 или 2): '))
        else:
            break
    return result

# Функция расчитывает перевод валюты
def convert(money, value):
    if value == 1:
        result = money / DOLLAR
    elif value == 2:
        result = money / EURO
    return result

# Функция выводит результат перевода
def print_result(result, value):
    if value == 1:
        print(f'Результат: {result:.2f}$')
    elif value == 2:
        print(f'Результат: {result:.2f}€')
        
        
if __name__ == '__main__':
    main()