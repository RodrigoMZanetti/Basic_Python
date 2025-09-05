from datetime import date
atual=date.today().year
data=int(input('Digite o ano de nascimento: '))
idade=atual-data
if idade<=9:
    print(f'O atleta tem {idade} anos, portanto ele está na categoria MIRIM.')
elif idade <=14:
    print(f'O atleta tem {idade} anos, portanto ele está na categoria INFANTIL.')
elif idade <=19:
    print(f'O atleta tem {idade} anos, portanto ele está na categoria JUNIOR.')
elif idade <=25:
    print(f'O atleta tem {idade} anos, portanto ele está na categoria SÊNIOR.')
elif idade >25:
    print(f'O atleta tem {idade} anos, portanto ele está na categoria MASTER.')

