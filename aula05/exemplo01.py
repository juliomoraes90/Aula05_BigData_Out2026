pedido_valor = float(input('Valor do pedido: '))
distancia_entrega = float(input('Distancia para entrega em KM: '))
taxa_entrega = 8

if distancia_entrega <= 3 and pedido_valor > 50:
    print(f'Frete Grátis')
    print(f'Valor total a pagar: R${pedido_valor:.2f}')
else:
    valor_final = pedido_valor + taxa_entrega
    print(f'Frete de R${taxa_entrega:.2f}')
    print(f'Valor total a pagar: R${valor_final:.2f}')
