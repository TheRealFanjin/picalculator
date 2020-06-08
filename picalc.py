import time
import decimal

def findpi(accuracy, numOfDigits):
    decimal.getcontext().prec = numOfDigits + 1
    x = decimal.Decimal('0')
    pidigits = decimal.Decimal('3')
    loopnum = 0
    add = True
    while True:
        loopnum += 1
        # outputs stat to console
        if loopnum % accuracy != 0:
            print('Checking for accuracy...')
        else:
            print('Waiting to log to pidigits.txt...')
        x += decimal.Decimal('2')
        x2 = x + decimal.Decimal('1')
        x3 = x + decimal.Decimal('2')
        multiply = x * x2 * x3
        divide = decimal.Decimal('4') / multiply
        if add:
            pidigits = decimal.Decimal(pidigits + divide)
            add = False
        else:
            pidigits = decimal.Decimal(pidigits - divide)
            add = True
        listedpidigits = list(str(pidigits))
        if loopnum % accuracy == 0:
            try:
                pidigit = int(listedpidigits[int(loopnum / accuracy + 1)])
            except:
                print('Max number reached')
                break
            with open('pidigits.txt', 'a') as file:
                file.write('%d' % pidigit)
                print('Log Successful')
            time.sleep(1)
userAccuracy = int(input('Type the accuracy (Amount of loops before it writes to file): '))
digits = int(input("Type the number of digits to solve for: "))
findpi(userAccuracy, digits)
