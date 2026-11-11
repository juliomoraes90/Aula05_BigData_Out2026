print ('''
[Codigo 1] Sul
[Codigo 2] Norte
[Codigo 3] Leste
[Codigo 4] Oeste
[Codigo 5] Nordeste
[Codigo 7,8 ou 9] Sudeste
[Codigo 10] Centro-Oeste
[Codigo 11] Noroeste
''')

cod = int(input('Insira o codigo da regiao: '))

match cod:
    case 1: print('Sul')
    case 2: print('Norte')
    case 3: print('Leste')
    case 4: print('Oeste')
    case 5 | 6: print('Nordeste')
    case cod if 7 <= cod <= 9: print('Sudeste')
    case 10: print('Centro-Oeste')
    case 11: print('Noroeste')
    case _: print('Importado')