# Программа выводит кол-во имен в файле names.txt

def main():
    total = 0
    names_file = open('names.txt', 'r')
    for line in names_file:
        amount = names_file.readline()
        total += 1
    print(f'Кол-во имен: {total}')
    
    names_file.close()
    
if __name__ == '__main__':
    main()