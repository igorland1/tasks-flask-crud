# Exemplo de uma função simples
def saudacao(nome):
    print(f"Olá, {nome}!")

# Testando a função
print("Chamando a função saudacao:")
saudacao("Mundo")
saudacao("Python")
saudacao("Desenvolvedor")

# Exemplo de uma função com retorno
def quadrado(numero):
    resultado = numero ** 2
    return resultado

# Testando a função com retorno e armazenando os resultados
resultado1 = quadrado(33)
resultado2 = quadrado(99)
resultado3 = quadrado(255)

# Apresentando os resultados
print("\nChamando a função quadrado:")
print("Resultado do teste 1:", resultado1)
print("Resultado do teste 2:", resultado2)
print("Resultado do teste 3:", resultado3)

# Exemplo de uma função com múltiplos parâmetros
def soma(numero1, numero2):
    return numero1 + numero2

numero1 = 10
numero2 = 20

# Testando a função com múltiplos parâmetros
resultado_soma = soma(numero1, numero2)
print("\nChamando a função soma:")
print("Resultado da soma de %s e %s é: %s" % (numero1, numero2, resultado_soma))
# É possível usar f-strings
print(f"Resultado da soma de {numero1} e {numero2} é: {resultado_soma}")
# E também a função format
print("Resultado da soma de {} e {} é: {}".format(numero1, numero2, resultado_soma))