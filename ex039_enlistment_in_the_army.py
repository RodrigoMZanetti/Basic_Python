from datetime import date
atual=date.today().year
data=int(input('Digite seu ano de nascimento: '))
genero=int(input('''
[1] Feminino
[2] Masculino
Qual é seu gênero: '''))
idade=atual-data
if genero==1:
    print('Você não precisa fazer alistamento obrigatório.')
elif genero==2 and idade == 18:
    print('Você está na idade de se alistar.')
elif genero==2 and idade >18:
    saldo=idade-18
    print('Já passou da idade de se alistar.')
    print(f'Você deveria ter se alistado em {saldo} ano (s).')
elif genero==2 and idade < 18:
    saldo = 18 - idade
    print('Você ainda não está na idade de se alistar.')
    print(f'Você tem ainda {saldo} ano (s) para se alistar.')