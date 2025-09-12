# Condição Verdadeira
verdadeiro = True
print(verdadeiro)  # Saída: True

# Condição Falsa
falso = False
print(falso)  # Saída: False

# Se Condição
if verdadeiro:
    print("A condição é verdadeira!")  # Saída: A condição é verdadeira!
else:
    print("A condição é falsa!")

# Operadores lógicos: and e or

a = True
b = False
print(a and b)  # Saída: False
print(a or b)   # Saída: True

# AND
if True and True:
    print("Ambas as condições são verdadeiras!")  # Saída: Ambas as condições são verdadeiras!

if True and False:
    print("Uma condição é verdadeira!") # Não será executado

if False and False:
    print("Nenhuma condição é verdadeira!") # Não será executado

# OR
if True or True:
    print("Pelo menos uma condição é verdadeira!")  # Saída: Pelo menos uma condição é verdadeira!

if True or False:
    print("Pelo menos uma condição é verdadeira!")  # Saída: Pelo menos uma condição é verdadeira!

if False or False:
    print("Nenhuma condição é verdadeira!") # Não será executado