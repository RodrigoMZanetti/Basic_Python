print("-"*20)
print("MÉDIA MAIOR E MENOR")
print("-"*20)

usuario="SIM"
lista=[]
numero = 0
media=0
maior=0
menor=0

while usuario == "SIM":
    try:
        numero = int(input("Digite um valor: "))
        lista.append(numero)
        usuario = str(input("Você deseja digitar mais um número? [SIM] ou [NAO]: ")).upper()
        while usuario != "SIM" and usuario != "NAO":
            print("CÓDIGO INVÁLIDO!")
            usuario = str(input("Você deseja digitar mais um número? [SIM] ou [NAO]: ")).upper().strip()
    except:
        print("ERRO você deve digitar um número válido")

print("Fim do programa e os resultados são ")
print(f"Os números digitados foram: {lista}")

if len(lista) > 0:
    maior = max(lista)
    menor = min(lista)
    media = (sum(lista) / len(lista))
    print(f"Você digitou {len(lista)} números.")
    print(f"O maior número digitado foi: {maior}.")
    print(f"O menor número digitado foi: {menor}.")
    print(f"A média dos números foi de: {media}.")
else:
    print("Não foi possível calcular o maior, menor e média por falta de números a lista.")