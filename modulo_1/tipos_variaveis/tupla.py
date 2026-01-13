# Tupla

# Tupla é uma coleção de dados imutável
# Tuplas são definidas com parênteses
minha_tupla = (1, 2, 2, 3, 4)

print(minha_tupla)
print(type(minha_tupla))

# Método count() retorna o número de vezes que um valor aparece na tupla
print(minha_tupla.count(2))  # Saída: 2

# Método index() retorna o índice da primeira ocorrência de um valor na tupla
print(minha_tupla.index(3))  # Saída: 3

# Tuplas podem conter diferentes tipos de dados
minha_tupla_v2 = (1, "dois", 3.0, True)
print(minha_tupla_v2)