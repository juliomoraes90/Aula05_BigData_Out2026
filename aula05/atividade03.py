mensagem = 'Frete Gratis'
valor_compra = float(input('Valor da compra R$: '))
fidelidade = input('Tem cadastro no programa de fidelidade?[s/n] ').lower()[0]

if valor_compra > 200 or fidelidade == 's':
    print(mensagem)
    print(f'Valor final: {valor_compra}')
else:
    valor_compra = valor_compra + 25
    print(f'Valor final: {valor_compra}')
