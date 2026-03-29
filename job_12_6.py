# Программа расчитывает среднее кол-во шагов за каждый месяц в году
JAN = 31
FEB = 28
MAR = 31
APR = 30
MAY = 31
JUN = 30
JUL = 31
AUG = 31
SEP = 30
OCT = 31
NOV = 30
DEC = 31

def main():
    #total_num = 0
    total_sum = 0
    stepsFile = open('steps.txt', 'r')
    
    for line in stepsFile:
        line = int(stepsFile.readline())
        #total_num += 1
        total_sum += line
        if file == 31:
            totalJAN = total_sum
            averageJAN = total_JAN / JAN
         elif file == 59:
            totalFEB = total_sum - totalJAN
            averageFEB = totalFEB / FEB
         elif file == 90:
            totalMAR = total_sum - totalJAN
            averageMAR = totalMAR / MAR
         elif file == 120:
             totalAPR = total_sum - totalMAR
             averageAPR = totalAPR / APR
         elif file == 151: 
             totalMAY = total_sum - totalAPR
             averageMAY = totalMAY / MAY
         elif file == 181:
              totalJUN = total_sum - totalMAY
              averageJUN = totalJUN / JUN
          elif file == 212:
              totalJUL = total_sum - totalJUN
              averageJUL = totalJUL / JUL
          elif file == 243: 
              totalAUG = total_sum - totalJUL
              averageAUG = totalAUG / AUG
          elif file == 273:
              totalSEP = total_sum - totalAUG
              averageSEP = totalSEP / SEP
          elif file == 304:
              totalOCT = total_sum - totalSEP
              averageOCT = totalOCT / SEP
          elif file == 334:
              totalNOV = total_sum - totalOCT
              averageNOV = totalNOV / NOV
          else:
              totalDEC = total_sum - totalNOV
              averageDEC = totalDEC / DEC
              
    stepsFile.close()
    display()

# Заготовки под будущие функции но сначала проверю код выше без функций
def get_JAN()
def get_FEB()
def get_MAR()
def get_APR()
def get_MAY()    
def get_JUN()
def get_JUL()
def get_AUG()
def get_SEP()
def get_OCT()
def get_NOV()
def get_DEC()

def display():
    print(f'Среднее кол-во шагов за Январь: {avrageJAN}')
    print(f'Среднее кол-во шагов за Февраль: {avrageFEB}')
    print(f'Среднее кол-во шагов за Март: {avrageMAR}')
    print(f'Среднее кол-во шагов за Апрель: {avrageAPR}')
    print(f'Среднее кол-во шагов за Май: {avrageMAY}')
    print(f'Среднее кол-во шагов за Июнь: {avrageJUN}')
    print(f'Среднее кол-во шагов за Июль: {avrageJUL}')
    print(f'Среднее кол-во шагов за Август: {avrageAUG}')
    print(f'Среднее кол-во шагов за Сентябрь: {avrageSEP}')
    print(f'Среднее кол-во шагов за Октябрь: {avrageOCT')
    print(f'Среднее кол-во шагов за Ноябрь: {avrageNOV}')
    print(f'Среднее кол-во шагов за Декабрь: {avrageDEC}')
    
if __name__ == '__main__':
    main()