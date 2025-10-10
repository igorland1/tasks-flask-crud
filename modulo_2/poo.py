# POO (Programação Orientada a Objetos)

# Classe Exemplo
class Pessoa:
    def __init__(self, nome, idade) -> None:
        self.nome = nome
        self.idade = idade

    def saudacao(self):
        return f"Olá, meu nome é {self.nome} e eu tenho {self.idade} anos de idade."

# Objetos
pessoa1 = Pessoa("João", 30)
pessoa2 = Pessoa(nome="Maria", idade=25)
# print("Nome:", pessoa1.nome)  # Saída: João
# print("Idade:", pessoa2.idade)  # Saída: 25

mensagem = pessoa1.saudacao()
print(mensagem)  # Saída: Olá, meu nome é João e eu tenho 30 anos de idade.

mensagem = pessoa2.saudacao()
print(mensagem)  # Saída: Olá, meu nome é Maria e eu tenho 25 anos de idade.