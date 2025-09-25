pesos = []

for pess in range (1, 6):
    peso=float(input(f'\033[1mQual o peso da {pess}ª pessoa?: \033[m'))
    pesos.append(peso)

print(f'\033[0;31mO maior peso lido foi {max(pesos):.2f} kg.\033[m')
print(f'\033[0;34mO menor peso lido foi {min(pesos):.2f} kg.\033[m')
