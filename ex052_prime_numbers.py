num=int(input('Enter a number: '))
tot=0
for c in range (1,num+1):
    if num % c == 0:
        print('\033[33m', end='')
        tot+=1
    else:
        print('\033[m', end='')
    print(f'{c}', end=' ')
print(f'\n\033[mO número {num} foi dividido {tot} vezes')
if tot == 2:
    print(f'O número {num} é primo')
else:
    print(f'O número {num} não é primo')