from time import sleep

somaidade = 0
mediaidade = 0
maioridade = 0
nomevelho = ''
totmulher20 = 0

for p in range (1,5):
    print(f'----- {p}ª PESSOA -----')
    nome=str(input('Nome: ')).strip()
    idade=int(input('idade: '))
    sexo=str(input('Sexo [M/F]: ')).strip()
    somaidade+=idade
    if p==1 and sexo in 'Mm':
        maioridadehomem=idade
        nomevelho=nome
    if sexo in 'Mm' and idade>maioridadehomem:
        maioridadehomem=idade
        nomevelho=nome
    if sexo in 'Ff' and idade<20:
        totmulher20+=1

print('Analisando dados das pessoas')
sleep(0.5)
print('.')
sleep(0.5)
print('.')
sleep(0.5)
print('.')

mediaidade=somaidade/4
print(f'\033[1mA média de idade do grupo é {mediaidade}\033[m')
print(f'\033[1;34mO homem mais velho do grupo é {nomevelho} e ele tem {maioridadehomem}\033[m')
print(f'\033[1;31mAo todo são {totmulher20} mulheres com menos de 20 anos.\033[m')
