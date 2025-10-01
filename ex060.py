n=int(input("Digite um número para calcular seu fatorial: "))

if n == 0 or n == 1:
    print(f"{n}! = 1")
else:
    f=1

    for c in range (n,0, -1):
        print(f"{c}", end='')
        print(' x ' if c > 1 else ' = ', end='')
        f *= c

    print(f"{f}")
