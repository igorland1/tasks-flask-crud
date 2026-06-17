# @classmethod
# @staticmethod

class MinhaClasse:
    valor = 10 # Atributo da Classe

    def __init__(self, nome) -> None:
        self.nome = nome # Atributo da Instância

    # Requer uma instância para ser chamado
    def metodo_instancia(self):
        return f"Método de instância chamado para {self.nome}"
    
    @classmethod
    def metodo_classe(cls):
        return f"Método de classe chamado para valor = {cls.valor}"
    
    @staticmethod
    def metodo_estatico():
        return "Método estático chamado"
    
obj = MinhaClasse(nome="Classe Exemplo")
print(obj.metodo_instancia())
print(MinhaClasse.valor)
print(MinhaClasse.metodo_classe())
print(MinhaClasse.metodo_estatico())

class Carro:
    def __init__(self, marca, modelo, ano) -> None:
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    @classmethod
    def criar_carro(cls, configuracao):
        marca, modelo, ano = configuracao.split(",")
        return cls(marca, modelo, int(ano))

configuracao1 = "Honda,Civic,2025"
carro1 = Carro.criar_carro(configuracao1)
print(f"Marca: {carro1.marca} Modelo: {carro1.modelo} Ano: {carro1.ano}")

