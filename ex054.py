from datetime import datetime, date
atual=date.today().year
totalmaior=0
totalmenor=0
for pess in range (1, 8):
    nascimento=int(input('Qual a data de nascimento? '))
    idade=atual-nascimento
    if idade >=21:
        totalmaior+=1
    else:
        totalmenor+=1
print(f'\033[0;34mAo todo tivemos {totalmaior} pessoas maiores de idade.\033[m')
print(f'\033[0;31mAo todo tivemos {totalmenor} pessoas menores de idade.\033[m')