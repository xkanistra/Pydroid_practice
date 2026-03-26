# Программа выводит сумму чисел а файле numbers.txt

def main():
    total = 0
    numbers_file = open('numbers.txt', 'r')
    for line in numbers_file:
        file = float(numbers_file.readline())
        total += file
    print(total)
    numbers_file.close()

if __name__ == '__main__':
    main()

          