from time import sleep
primeiro=int(input('Primeiro numero: '))
razao=int(input('Razão: '))
decimo=primeiro+(10-1)*razao
for c in range (primeiro,decimo+razao,razao):
    print(f'{c}',end='\033[1m->\033[m ')
    sleep(0.5)
print('END')