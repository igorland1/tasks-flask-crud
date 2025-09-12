# Exemplo de while loop em Python
contador = 0
while contador < 5:
    print("Contador:", contador)
    contador += 1 # Outra forma de incrementar o contador é usar: contador = contador + 1
print("Loop terminado!")


# Exemplo de while loop com break
contador = 0
while True:
    print("Contador infinito:", contador)
    contador += 1
    if contador >= 5:
        print("Condicional de parada atingida, saindo do loop.")
        break