# Estruturas de repetição - for
lista = [1, 2, 3, 4, 5]
for elemento in lista:
    print(elemento)

# Tuplas são semelhantes às listas, mas são imutáveis
print("Isso é um separador")
tupla = (1, 2, 3, 4, 5)
for elemento in tupla:
    print(elemento)

# Dicionários são estruturas de dados que armazenam pares de chave-valor
pessoa = {"nome": "João", "idade": 30, "cidade": "São Paulo"}
print("\nFor usando dicionário - Chaves")
for chave in pessoa.keys():
    print(chave)

print("\nFor usando dicionário - Chaves")
for valor in pessoa.values():
    print(valor)

print("\nFor usando dicionário - Itens")
for chave, valor in pessoa.items():
    print(f"{chave}: {valor}")

# range() é usado para gerar uma sequência de números dentro de um intervalo especificado
print("\nFor usando range")
numero = [1, 2, 3, 4, 5]
for numero in range(5):  # 0 a 4
    print("Número:", numero)

# range() e len() juntos para iterar sobre índices de uma lista
print("\nUtilizando a função range() com len()")
lista = [1, 2, 3, 4, 5]
print(lista)
for indice in range(0, len(lista)):
    if indice == 3:
        lista[indice] = 5
    else:
        lista[indice] = 0
print(lista)

#enumerate() é uma função embutida que adiciona um contador a um iterável e retorna um objeto enumerado
print("\nUtilizando a função enumerate()")
lista = ['a', 'b', 'c', 'd', 'e']
for indice, valor in enumerate(lista):
    print(f"Índice: {indice}, Valor: {valor}")