mensagem = 'Frete Gratis'
valor_compra = float(input('Valor da compra R$: '))
fidelidade = input('Tem cadastro no programa de fidelidade?[s/n] ').lower()[0]
FRETE = 25

if valor_compra > 200 or fidelidade == 's':
    print(mensagem)
    print(f'Valor final R$: {valor_compra}')
else:
    valor_compra = valor_compra + FRETE
    mensagem = 'Valor frete R$: 25,00'
    print(mensagem)
    print(f'Valor final R$: {valor_compra}')
