# Declaração de lista

minha_lista = [1, 2, 3, 4, 5]
print(minha_lista)

# Declarar apenas 1 item
minha_lista = [1, 2, 3, 4, 5]
print(minha_lista[2])  # Acessa o item na posição 2 (terceiro item)

# Declarar utilizando informações da lista
minha_nova_lista = ["Igor", 20, "Rocketseat", 3.14, True]
print("Meu nome é", minha_nova_lista[0], "tenho", minha_nova_lista[1], "anos e estudo na", minha_nova_lista[2],"!")

print("Número do PI é", minha_nova_lista[3], "e é", minha_nova_lista[4], "que eu estudo na Rocketseat!")

# Exibindo os elementos da lista
print("minha_lista[0]:", minha_lista[0])
print("minha_lista[1]:", minha_lista[1])
print("minha_lista[2]:", minha_lista[2])
print("minha_lista[3]:", minha_lista[3])
print("minha_lista[4]:", minha_lista[4])

print("minha_lista[1:4]:", minha_lista[1:4])  # Acessa do índice 1 ao 3 (4-1)
print("minha_lista[:3]:", minha_lista[:3])    # Acessa do início ao índice 2 (3-1)
print("minha_lista[2:]:", minha_lista[2:])    # Acessa do índice 2 até o final

minha_lista[0] = "Python" # Alterando o valor do primeiro item
print(minha_lista[0])
print(minha_lista)

# Método append(): Adiciona um item ao final da lista
minha_lista.append(6)
print("Após append(6):", minha_lista)

# Método index(): Retorna o índice do primeiro item com o valor especificado
indice = minha_lista.index(6)
print("Índice do valor 6:", indice)

# Método insert(): Insere um item em uma posição específica
minha_lista.insert(0, "Início")
print("Após insert(0, 'Início'):", minha_lista)
print(minha_lista[0])
print(minha_lista[1])
print(minha_lista[2])
print(minha_lista[3])
print(minha_lista[4])
print(minha_lista[5])
print(minha_lista[6])

# Método pop(): Remove e retorna o último item da lista
ultimo_item = minha_lista.pop()
print("Após pop():", minha_lista)
print("Item removido:", ultimo_item)

# Método remove(): Remove a primeira ocorrência do valor especificado
minha_lista.remove("Início")
print("Após remove('Início'):", minha_lista)

# Função len(): Retorna o número de itens na lista
tamanho = len(minha_lista)
print("Tamanho da lista usando len():", len(minha_lista))
print(minha_lista)

# Função sum(): Retorna a soma dos itens da lista (apenas para listas numéricas)
lista_numerica = [1, 2, 3, 4, 5]
soma = sum(lista_numerica)
print("Soma dos itens da lista_numerica usando sum():", soma)
print(lista_numerica)

# Função sorted(): Retorna uma nova lista ordenada
lista_desordenada = [3, 1, 4, 2, 5]
lista_ordenada = sorted(lista_desordenada)
print("Lista desordenada:", lista_desordenada)
print("Lista ordenada usando sorted():", lista_ordenada)
print(lista_desordenada)

# Método sort(): Ordena a lista no local
lista_desordenada.sort()
print("Lista desordenada após sort():", lista_desordenada)
print(lista_desordenada)