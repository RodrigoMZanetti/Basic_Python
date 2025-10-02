from time import sleep

print("=*=*"*20)
print("Calculadora de PA")
print("=*=*"*20)

numero=int(input("\033[1mDigite o primeiro termo da PA: \033[m"))
razao=int(input("\033[1mAgora digite a razão da PA: \033[m"))
componentes=int(input("\033[1mQuantos termos você quer da PA?: \033[m"))

print("O computador está pensado...\U0001F92F")
sleep(2)

c=0
termo=numero

print(f"\033[34mA PA do número {numero} com a razão de {razao} é:\033[m \033[33m{numero}\033[m, ", end="")
while c != (componentes-1):
    termo=termo+razao
    print(f"\033[33m{termo}\033[m", end=", "if c<(componentes-2) else"")
    c+=1
