# Exemplo de Heritage (Herança)
class Animal:
    def __init__(self, nome):
        self.nome = nome

    def andar(self):
        print(f"{self.nome} está andando.")
        return

    def fazer_som(self):
        pass

class Cachorro(Animal):
    def fazer_som(self):
        return "Au, Au"
    
class Gato(Animal):
    def fazer_som(self):
        return "Miau!"
    
dog = Cachorro(nome="Rex")
cat = Gato(nome="Felix")

print("\nExemplo de polimorfismo")
animais = [dog, cat]

for animal in animais:
    print(f"{animal.nome} diz: {animal.fazer_som()}")