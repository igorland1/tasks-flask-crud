# if, elif e else

# Exemplo de uso do if
idade = 18
if idade >= 18:
    print("Você é maior de idade.")

# Exemplo de uso do if e else
idade = 16
if idade >= 18:
    print("Você é maior de idade.")
else:
    print("Você é menor de idade.")

# Exemplo de uso do if, elif e else
nota = 85
if nota >= 90:
    print("Você recebeu um A.")
elif nota >= 80:
    print("Você recebeu um B.")
elif nota >= 70:
    print("Você recebeu um C.")
else:
    print("Você precisa melhorar.")

# Exemplo de ==
numero = 10
print("O número é igual a 10.")

# Exemplo de >= e <=
numero = 5
if numero >= 5:
    print("O número é maior ou igual a 5.")
if numero <= 10:
    print("O número é menor ou igual a 10.")

# Exemplo de !=
letra = 'a'
if letra != 'b':
    print("A letra não é 'b'.")

# Exemplo de input e condicional em linha única

numerao = int(input("Digite sua idade: "))
mensagem = "Pode tirar CNH" if numerao >= 18 else "Não pode tirar CNH"
print(mensagem)