nota01 = float(input('Insira a Nota da avaliação 01: '))
nota02 = float(input('Insira a Nota da avaliação 02: '))
nota03 = float(input('Insira a Nota da avaliação 03: '))
nota04 = float(input('Insira a Nota da avaliação 04: '))

media = (nota01 + nota02 + nota03 + nota04) / 4

print(f'Nota final: {media:.1f}')

if media >= 7:
    print('Aprovado')
elif media >=5 and media < 7:
    print('Recuperação')
else:
    print('Reprovado')