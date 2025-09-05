num=int(input('Digite um número inteiro: '))
print('''Escolha uma das bases para conversão
[1] Converter para binário
[2] Converter para octal
[3] Converter para hexadecimal''')
opção=int(input('Sua opção: '))
if opção==1:
    print(f'{num:.1f} convertido para binário é igual {bin(num)[2:]}')
elif opção==2:
    print(f'{num:.1f} convertido para octal é igual {oct(num)[2:]}')
elif opção==3:
    print(f'{num:.1f} convertido para hexadecimal é igual {hex(num)[2:]}')
else:
    print('Opção inválida, escolha novamente.')

