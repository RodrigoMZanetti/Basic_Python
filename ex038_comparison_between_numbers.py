numum=int(input('Digite um número inteiro: '))
numdois=int(input('Digite um segundo número inteiro: '))
if numum > numdois:
    print(f'O número {numum} é maior que {numdois}.')
elif numdois > numum:
    print(f'O numéro {numdois} é maior que {numum}.')
elif numum == numdois:
    print(f'Não existe maior, os dois são iguais.')

