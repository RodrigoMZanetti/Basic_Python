from random import randint
from time import sleep

computador = randint(0, 10)
print('\033[1mSou seu computador e irei pensar em um número entre 0 a 10!\033[m')
sleep(1)
print('\033[1mTente adivinhar!\033[m')

acertou=False
palpites=0

while not acertou:
    jogador=int(input('\033[1;34mQual é seu palpite?:\033[m '))
    palpites+=1

    if jogador == computador:
        acertou=True

    else:
        if jogador < computador:
            print('\033[1;31mQuase! Tente um valor um pouco maior!\033[m')
        elif jogador > computador:
            print('\033[1;31mQuase! Tente um valor um pouco menor!\033[m')

print(f'\033[1;33mPARABÉNS! Você acertou em {palpites} tentativas!!!\033[m')
