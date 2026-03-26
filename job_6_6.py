# Программа выводит среднее арифметическое чисел а файле numbers.txt

def main():
    total_line = 0
    total_numbers = 0
    numbers_file = open('numbers.txt', 'r')
    for line in numbers_file:
        file = float(numbers_file.readline())
        total_numbers += file
        total_line += 1
    average = total_numbers / total_line
    print(average)
    numbers_file.close()

if __name__ == '__main__':
    main()