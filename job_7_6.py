# Программа записывает случайные числа в файл с возможность контролировать кол-во чисел в файле

import random

def main():
    amount = int(input('Введите кол-во чисел записываемых в файл: '))
    file = open('random_num', 'w')
    number = random.randint(1, 500)
    for i in range(1, amount + 1):
        file.write(f'{number}\n')
        
    print(f'Данные в файл сохранены')
    file.close()
    
if __name__ == '__main__':
    main()
    
        
        