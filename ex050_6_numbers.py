from time import sleep
soma=0
cont=0
for i in range (1,7):
    num=int(input(f'Write the {i} number: '))
    sleep(0.2)
    if num%2==0:
        soma+=num
        cont+=1
print(f'\033[1;31;43mthe sum of {cont} even numbers is equal to {soma}\033[m')