import random
from time import sleep

print('|=|'*20)
escolha=int(input('''What's your choice?: 
[1] Rock
[2] Paper
[3] Scissors
Your choice is: '''))
if escolha == 1:
    escolha='Rock'
    print(f'Sua escolha foi {escolha}')

elif escolha == 2:
    escolha='Paper'
    print(f'Sua escolha foi {escolha}')

elif escolha == 3:
    escolha='Scissors'
    print(f'Sua escolha foi {escolha}')

else:
    print('Sua escolha invalida!')
    raise SystemExit

print('🖥️ Computer is thinking')
sleep(2)

computer_choice=random.choice(['Rock','Paper','Scissors'])
print(f'The computer choice: {computer_choice}')

if computer_choice == escolha:
    print('🤝\033[1;30;43mIt is a tie!\033[m')
elif (computer_choice == 'Rock' and escolha == 'Paper') or (computer_choice == 'Paper' and escolha == 'Scissors') or (computer_choice == 'Scissors' and escolha == 'Rock'):
    print('🏆\033[1;30;42mYou win!\033[m')
else:
    print('💀\033[1;30;41mYou lose!\033[m')





