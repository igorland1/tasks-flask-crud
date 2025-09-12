# Criando um dicionário com informações de uma pessoa
pessoa = {"nome": "João", "idade": 30, "cidade": "São Paulo"}

# Dicionario é uma coleção de pares chave-valor

# Acessando valores do dicionário
print("Nome:", pessoa["nome"])
print("Idade:", pessoa["idade"])
print("Cidade:", pessoa["cidade"])

# Adicionando uma nova chave e valor ao dicionário
pessoa["profissão"] = "Engenheiro"

# Imprimindo o dicionário atualizado
print("Dicionário atualizado:", pessoa)

# Verificando se uma chave existe no dicionário
if "idade" in pessoa:
    print("A chave 'idade' existe no dicionário.")
else:
    print("A chave 'idade' não existe no dicionário.")

# Removendo uma chave do dicionário
del pessoa["cidade"]
print("Dicionário após remoção da chave 'cidade':", pessoa)

# Verificando se uma chave existe no dicionário
if "cidade" in pessoa:
    print("A chave 'cidade' existe no dicionário.")
else:
    print("A chave 'cidade' não existe no dicionário.")

# Métodos: keys(), values(), items()
print("Chaves:", pessoa.keys())
print("Valores:", pessoa.values())
print("Itens:", pessoa.items())

# Convertendo as chaves do dicionário em uma lista
chaves_lista = list(pessoa.keys())
print("Chaves como lista:", chaves_lista)
# Convertendo os valores do dicionário em uma lista
valores_lista = list(pessoa.values())
print("Valores como lista:", valores_lista)
# Convertendo os itens do dicionário em uma lista de tuplas
itens_lista = list(pessoa.items())
print("Itens como lista de tuplas:", itens_lista)
print("Primeira chave-valor: %s = %s" % (itens_lista[0][0], itens_lista[0][1]))