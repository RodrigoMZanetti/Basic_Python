from time import sleep
numero = int(input('Which multiplication table would you like to learn? The multiplication table of: '))
print('-'*20)
for multiplicador in range(1,11):
    resultado = numero * multiplicador
    print(f'{numero} x {multiplicador} = {resultado}')
    sleep(0.3)
print('\033[1;40;42m-\033[m'*20)