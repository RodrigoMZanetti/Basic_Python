reta1=float(input('Qual é a dimensão da reta 1: '))
reta2=float(input('Qual a dimensão da reta 2: '))
reta3=(float(input('Qual a dimensão da reta 3: ')))

if (reta1 + reta2 > reta3) and (reta2 + reta3 > reta1) and (reta1 + reta3 > reta2) and (reta1 == reta2) and (reta2 == reta3):
    print(f'Com as retas {reta1}, {reta2} e {reta3} você pode formar um triângulo, e ele é um triângulo EQUILATERO.')

elif (reta1 + reta2 > reta3) and (reta2 + reta3 > reta1) and (reta1 + reta3 > reta2) and ((reta1 == reta2) or (reta2 == reta3) or (reta3 == reta1)):
    print(f'Com as retas {reta1}, {reta2} e {reta3} você pode formar um triângulo, e ele é um triângulo ISÓSCELES.')

elif (reta1 + reta2 > reta3) and (reta2 + reta3 > reta1) and (reta1 + reta3 > reta2) and (reta1 != reta2) and (reta1 != reta3) and (reta2 != reta3):
    print(f'Com as retas {reta1}, {reta2} e {reta3} você pode formar um triângulo, e ele é um triângulo ESCALENO.')

else:
    print(f'Com as retas {reta1}, {reta2} e {reta3} você não pode formar um triângulo')
