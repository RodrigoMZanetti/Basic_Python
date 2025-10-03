from time import sleep

print("*-*"*20)
print("\033[1mSEQUÊNCIA FIBONACCI\033[m \U0001F60D ")
print("*-*"*20)

numero_1=int(input("\033[32mDigite um número para sua começar sequência Fibonacci:\033[m "))
numero_2=int(input("\033[33mAgora digite o segundo número da sequência:\033[m "))
componentes=int(input("\033[34mQuantos componentes da sequência você deseja?:\033[m "))

print("O computador está pensando... \U0001F914")
sleep (2)

if componentes==0:
    print("ERRO! Recomece e por favor digite um valor de componentes maior do que zero.")
elif componentes == 1:
    print(f"Sua sequência Fibonacci tem apenas 1 componente: {numero_1}.")
elif componentes == 2:
    S=numero_1+numero_2
    print(f"Sua sequência Fibonacci tem apenas 2 componenentes: {numero_1} e {numero_2} e a soma de todos os componentes é igual a {S}.")
elif componentes > 2:
    componente_1=numero_1
    componente_2=numero_2
    c=0
    componente=0
    S=numero_1+numero_2

    print(f"\U0001F92F \033[37mOs componentes da sequência Fibonacci solicitada são:\033[m {numero_1}, {numero_2},", end="")
    while c != componentes-2:
        componente=componente_1+componente_2
        componente_1 =componente_2
        componente_2=componente
        S+=componente
        c+=1
        print(f" {componente}", end="," if c<=componentes-3 else"")
    print(f" e a soma de todos os componentes é {S}.")
    print("MUITO OBRIGADO \U0001F60E ")

