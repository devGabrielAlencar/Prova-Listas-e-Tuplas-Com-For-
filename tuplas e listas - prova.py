
pares = []
impar = []

for usuario in range(10):

    print("\ndigite ate 10 valores")
    usuario = float(input(f"valor {usuario+1}: "))

    if usuario % 2 == 0:
        pares.append(usuario)

    else:
        impar.append(usuario)

tupla_impar = tuple(impar)
qntd_pares = len(pares)
qntd_impar = len(impar)
soma_pares = sum(pares)
soma_impar = sum(impar)

print(f"\nOs números pares inseridos são : {pares}")
print(f"\nOs números impares inserdos são: {tupla_impar}")
print(f"\n A quantidade de números par é: {qntd_pares}")
print(f"\n A quantidade de números impar é: {qntd_impar}")
print(f"\n A soma dos números pares é: {soma_pares}")
print(f"\n A soma dos números impar é: {soma_impar}")
