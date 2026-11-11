num = float(input('Digite o numero: '))

match num:
    case num if 0 < num: print('Positivo')
    case num if 0 > num: print('Negativo')
    case 0: print('ZERO')