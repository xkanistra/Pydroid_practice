# Программа выводит содержимое файла с нумеровкой строк

def main():
    filename = input('Введите имя файла: ')
    file = open(filename, 'r')
    total = 0
    for line in file:
        amount = file.readline()
        total +- 1
        print(f'{total}. {amount}')
    file.close()
    
if __name__ == '__main__':
    main()