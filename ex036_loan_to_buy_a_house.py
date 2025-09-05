valor=float(input('Qual o valor da casa? '))
salario=float(input('Qual seu salário? '))
ano=float(input('Em quantos anos você vai pagar? ' ))
prestaçoes=ano*12
pagamento=valor/prestaçoes
print(f'Você vai pagar em {prestaçoes:.1f} prestações de {pagamento:.3f} reais.')
limite=salario*0.3
if pagamento<=limite:
    print('O empréstimo foi autorizado!')
else:
    print('O empréstimo não foi autorizado!')
