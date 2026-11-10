nota_final = float(input('Nota Final: '))
frequencia = float(input('Frequencia do aluno: '))
mensalidade = float(input('Valor mensalidade: '))
valor_bolsa = 0.2 * mensalidade
mensalidade_pagar = mensalidade - valor_bolsa

if nota_final >= 7 and frequencia >= 75:
    print(f'Elegível para bolsa de: R${valor_bolsa:.2f}')
    print(f'Valor calculado da mensalidade: R${mensalidade_pagar:.2f}')
else:
    print('Nao elegível para bolsa')