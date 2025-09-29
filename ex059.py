escolha=0

def ler_numero(mensagem):
    while True:
        try:
            return int(input(mensagem))
        except ValueError:
            print("Opção inválida! Digite apenas números.")

escolha_1=ler_numero('\033[1mDigite o primeiro número: \033[m')
escolha_2=ler_numero('\033[1mDigite o segundo número: \033[m')

while escolha !=5:
    try:
        escolha=int(input('''\033[1;34mEscolha uma das opções 
        [1] soma
        [2] multiplicar
        [3] maior
        [4] novos números
        [5] sair do programa 
        
        Sua escolha é: \033[m'''))
    except ValueError:
        print("Opção inválida! Digite apenas números.")
        continue

    if escolha == 1:
        soma=escolha_1+escolha_2
        print(f'\033[1mA soma de {escolha_1} e {escolha_2} é {soma}.\033[m')

    elif escolha == 2:
        multiplicar=escolha_1*escolha_2
        print(f'\033[1mA multiplicação estre {escolha_1} e {escolha_2} é {multiplicar}\033[m')

    elif escolha == 3:
        if escolha_1 > escolha_2:
            print(f'\033[1;33mEntre os números {escolha_1} e {escolha_2}, {escolha_1} é o número maior.\033[m')
        elif escolha_2 > escolha_1:
            print(f'\033[1;3mEntre os números {escolha_1} e {escolha_2}, {escolha_2} é o número maior.\033[m')
        elif escolha_1==escolha_2:
            print(f'\033[1;33mEntre os números {escolha_1} e {escolha_2} não há maior.\033[m.')

    elif escolha == 4:
        escolha_1=ler_numero('\033[1mEscolha novamente o primeiro número: \033[m')
        escolha_2=ler_numero('\033[1mEscolha novamente o segundo número: \033[m')

    elif escolha == 5:
        print('\033[1;31mFim do programa, muito obrigado.\033[m')

    else:
        print('''\033[1;31mERRO, escolha inválida!\033[m''')



