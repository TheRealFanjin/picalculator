import time
from decimal import Decimal


def findpi(accuracy=10000):
    x = Decimal(0)
    pidigits = Decimal(3)
    loopnum = 0
    add = True
    while True:
        loopnum += 1
        # outputs stat to console
        if loopnum % accuracy != 0:
            print('Checking for accuracy...')
        else:
            print('Waiting to log to pidigits.txt...')
        x += Decimal(2)
        x2 = x + Decimal(1)
        x3 = x + Decimal(2)
        multiply = x * x2 * x3
        divide = Decimal(4) / multiply
        if add:
            pidigits = pidigits + divide
            add = False
        else:
            pidigits = pidigits - divide
            add = True
        #checking for accuracy
        listedpidigits = list(str(pidigits))
        print(pidigits)
        if loopnum % 100 == 0:
            print(pidigits)
        if loopnum % accuracy != 0:
            time.sleep(.01)
            continue

        else:
            pidigit = int(listedpidigits[int(loopnum / accuracy + 1)])
            try:
                pidigit = int(listedpidigits[int(loopnum / accuracy + 1)])
            except:
                print('Max number reached')
                break
            with open('pidigits.txt', 'a') as file:
                file.write('%d' % pidigit)
                print('Log Successful')
            time.sleep(.01)

input('Press enter to start:')
findpi()
