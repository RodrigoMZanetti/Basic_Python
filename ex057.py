from time import sleep

sexo=0

while sexo not in ('M','F'):
    sexo = str(input('Digite seu sexo [M/F]: ')).strip().upper()[0]
    sleep(0.5)
    if sexo == 'M':
        print(f'\033[0;34mSeu sexo é masculino.\033[m')
    elif sexo == 'F':
        print(f'\033[0;31mSeu sexo é feminino.\033[m')
    else:
        print('\033[1;31mResposta incorreta, por favor responda novamente!\033[m')
print('Obrigado')

