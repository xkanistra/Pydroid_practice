# Программа генерирует веб страницу HTML

import os

def main():
    found = False
    
    name = input('Введите свое имя: ')
    descr = input('Опишите себя: ')
    
    name_html = (f'\t\t<h1>{name}<h1>')
    descr_html = (f'\t<hr />\n{descr}\n\t<hr />')
    
    html_file = open('personal.html', 'r')
    temp_file = open('temp.html', 'w')
    
    for line in html_file:
        line = html_file.readline()
        
        line = line.rstrip('\n')
        
        if name_html == line:
            temp_file.write(f'{name_html}\n')
            temp_file.write(f'{descr_html}\n')
            found = True
            
        else:
            temp_file.write(f'{line}\n')
            temp_file.write(f'{line}\n')
        
    html_file.close()
    temp_file.close()
    
    os.remove('html_file')
    os.rename('temp_file', 'html_file')
    
    if found:
            print('Файл обнов.')
    else:
            print('Знач не найд')
            
if __name__ == '__main__':
    main()
            
            
            
            
        