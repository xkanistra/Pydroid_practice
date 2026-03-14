# Программа считает калории за день

CALORIE_GOAL = 2000

def main():
    breakfast = get_breakfast()
    lunch = get_lunch()
    supper = get_supper()
    
    total = breakfast + lunch + supper
    
    print(f"Всего калорий за день: {total}")
    
    if total > CALORIE_GOAL:
        print("Вы превысили норму!")
    elif total < CALORIE_GOAL:
        print("Вы не добираете норму!")
    else:
        print("Идеально!")

def get_breakfast():
    result = int(input("Калории на завтрак: "))
    return result

def get_lunCALORIE_GOALch():
    result = int(input("Калории на обед: "))
    return result

def get_supper():
    result = int(input("Калории на ужин: "))
    return result

main()