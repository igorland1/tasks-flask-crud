print("Exemplo de tratamento de exceções em Python")
try:
    numero = int(input("Digite um número inteiro: "))
    resultado = 10 / numero
except ValueError as e:
    print(f"Erro de ValueError: {e}")
    # raise ValueError("Quebrar o código propositalmente")
except Exception as e:
    print(f"Ocorreu um erro: {e}")
else:
    print(f"O resultado de 10 dividido por {numero} é {resultado}")
finally:
    print("Operação finalizada")