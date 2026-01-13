def meu_decorador(func):
    def wrapper():
        print("Client Offline")
        func()
        print("Client Loged")
    return wrapper

@meu_decorador
def minha_funcao():
    print("Client Loading!")

minha_funcao()

class MeuDecoradorDeClasse:
    def __init__(self, func) -> None:
        self.func = func

    def __call__(self) -> any:
        print("Antes da função ser chamada (Decorador de classe)")
        self.func()
        print("Depois da função ser chamada (Decorador de classe)")

@MeuDecoradorDeClasse
def segunda_funcao():
    print("Segunda função foi chamada")

segunda_funcao()