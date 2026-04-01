# Программа сохраняет историю каллорий

GOAL = 3000

def main():
    while True:
        choise = display()
        if choise == 1:
            date = input('Введите дату (ДД:ММ:ГГ): ')
            calories = get_calories()
            report = get_print_report(date, calories, GOAL)
            get_save_file(date, calories, GOAL)
        
        elif choise == 2:
            load_last_report()
        
        else:
             print('Программа законченна')
             break                                           
                
# Меню с выбором    
def display():
    print('=' * 3, 'Дневник калорий', '*' * 3)
    print(f'1. Новый день')
    print(f'2. История')
    print(f'3. Выход')
    choise = int(input('Выберите действие: '))
    while choise != 1 or choise != 2 or choise != 3:
        print('ОШИБКА. Не допустимое значение')
        choise = input('Введите допустимое значение(1, 2 или 3')
    return choise

# Расчет калорийности дня
def get_calories():
        breakfast = int(input('Калории за завтрак: '))
        lunch = int(input('Калории за обед: '))
        dinner = int(input('Калории за ужин: '))
        total = breakfast + lunch + dinner
        return total
       
# Вывод результата       
def get_print_report(date, calories, goal):
    if calories < goal:
        print(f'Итого за день {date}: {calories} ккал')
        print(f'Норма: {goal} ккал')
        print(f'Рекомендация: Вы не добираете норму на : {goal - calories}')
    elif calories > goal:
         print(f'Итого за день {date}: {calories} ккал')
         print(f'Норма: {goal} ккал')
         print(f'Рекомендация: Вы едите выше нормы на : {calories - goal}')
    else: 
        print(f'Итого за день {date}: {calories} ккал')
        print(f'Норма: {goal} ккал')
        print(f'Рекомендация: Вы едите ровно, молодцы!')
   
# Сохранение данных в файле   
def get_save_file(date, calories, goal):
    with open('calories_history.txt', 'a', encoding = 'utf-8') as save_file:
        if calories < goal:
            save_file.write(f'{date} | {calories} ккал | Ниже нормы')                                
        elif caloriea > goal:
            save_file.write(f'{date} | {calories} ккал | Выше нормы')            
        else:
            save_file.write(f'{date} | {calories} ккал | Норма')                   
    print('✅️Записано в calories_history.txt')
    
# Открытие файла для чтения
def load_last_report():
    with open('calories_history.txt', 'r', encoding = 'utf-8') as save_file:
        line = save_file.read()
        print(line)
       
        
    