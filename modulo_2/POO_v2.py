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


print("\nExemplo de Encapsulation (Encapsulamento)")
class ContaBancaria:
    def __init__(self, saldo_inicial):
        self.__saldo = saldo_inicial  # Atributo privado

    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
            print(f"Depósito de {valor} realizado. Novo saldo: {self.__saldo}")
        else:
            print("Valor de depósito inválido.")

    def sacar(self, valor):
        if 0 < valor <= self.__saldo:
            self.__saldo -= valor
            print(f"Saque de {valor} realizado. Novo saldo: {self.__saldo}")
        else:
            print("Saldo insuficiente ou valor inválido.")
        
    def obter_saldo(self):
        return self.__saldo

conta = ContaBancaria(1000)
print(f"\nSaldo atual: {conta.obter_saldo()}")
conta.depositar(500)
print(f"Saldo atual: {conta.obter_saldo()}")
conta.sacar(200)
print(f"Saldo atual: {conta.obter_saldo()}")
conta.sacar(2000)  # Tentativa de saque inválido
print(f"Saldo atual: {conta.obter_saldo()}")

conta_do_jose = ContaBancaria(300)
print(f"Saldo da conta do José: {conta_do_jose.obter_saldo()}")
conta_do_jose.depositar(150)
print(f"Saldo da conta do José: {conta_do_jose.obter_saldo()}")



print("\nExemplo de Abstraction (Abstração)")
from abc import ABC, abstractmethod

class Veiculo(ABC):
    
    @abstractmethod
    def ligar_motor(self):
        pass

    @abstractmethod
    def desligar_motor(self):
        pass

class Carro(Veiculo):
    def __init__(self) -> None:
        pass

    def ligar_motor(self):
        print("O motor do carro está ligado.")
    
    def desligar_motor(self):
        print("O motor do carro está desligado.")

meu_carro = Carro()
meu_carro.ligar_motor()
meu_carro.desligar_motor()