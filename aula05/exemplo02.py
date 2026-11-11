# Estrutura Match Case
print('''
[    1    ] Marketing
[    2    ] Financeiro
[  3 a 5  ] Administração
[  6 a 9  ] TI
[ 10 a 20 ] Serviços Gerais
''')

opcao = int(input('Informe o codigo do setor: '))

match opcao:
    case 1:
        print('Marketing')
    case 2:
        print('Financeiro')
    case 3 | 4 | 5:
        print('Admnistração')
    case opcao if 6 <= opcao <= 9:
        print('TI')
    case opcao if 10 <= opcao <= 20:
        print('Serviços Gerais')
    case _:
        print('Codigo inválido')
