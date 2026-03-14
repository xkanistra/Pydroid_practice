# Анализатор шагов

# Константа дней
DAY = 7

def main():
    total_steps = 0
    
    # Расчет шагов за 7 дней
    for i in range(1, DAY + 1):
        get_steps= int(input(f"Введите шаги за день {i}: "))
        total_steps += get_steps
        
    # Расчет среднего кол-ва шагов
    average = total_steps / DAY
    
    max_days = count_max_days(total_steps, average)
    
    print(f"Среднее: {average}")
    print(f"Дней выше среднего: {max_days}")

# Функция расчитывает кол-во дней, когда шагов было больше среднего
def count_max_days(total_steps, average):
    count = 0
    for steps in total_steps:
        if steps > average:
            count += 1
    return count

if __name__ == '__main__':
    main()