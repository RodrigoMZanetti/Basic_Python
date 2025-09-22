soma=0
contador=0
for num in range(1,501,2):
    if num % 3 == 0:
        soma = soma + num
        contador = contador + 1
print(f'\033[1;39;39mA soma dos {contador} números é {soma}\033[m')